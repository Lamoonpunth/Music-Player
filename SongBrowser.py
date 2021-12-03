from os import name
from re import S
import re
from kivy.core import text
from kivy.lang import Builder
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import BoxLayout
from kivy.uix.scatter import Scatter
from kivy.core.text import LabelBase
import os
# Add Font
LabelBase.register(name='sf',fn_regular='archive/finalFontV2.ttf')

Builder.load_file('SongBrowser.kv')

class Browser():
    choosed = None
    path = None
    class SongBrowser(BoxLayout):  
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            # self.choosed = None

        def selected(self,path,filename):
            Browser.choosed = filename
            Browser.path = path
            print(f'one clicked = {Browser.choosed}')

    class AddSong(MDFloatLayout):   
        def __init__(self, **kwargs):
            super(MDFloatLayout, self).__init__(**kwargs) 
            self.orientation='horizontal'
            self.size_hint=(None,None)   
            self.songbrowser = Browser().SongBrowser()
            self.box = None
            self.warning = None

        def show_songbrowser(self):
            if not self.box:
                self.box = MDDialog(                
                    type="custom",
                    content_cls = Browser().SongBrowser(),
                    buttons=[
                        MDFlatButton(
                            text="OK",
                            theme_text_color="Custom",
                            on_release = self.clickConfirm
                        ),
                        MDFlatButton(
                            text="CANCEL",
                            theme_text_color="Custom",              
                            on_release = self.clickCancel                           
                        ),
                    ],
                )
            self.box.open()
        
        def clickCancel(self,instance):
            self.box.dismiss()

        def clickConfirm(self,instance):
            song = Browser.choosed
            if song != None:
                song = song[0]
                name = os.path.join(Browser.path, Browser.choosed[0])[len(Browser.path)+1:]
                #archive/song/
                print(name)
                song = Browser.choosed[0]
                import shutil
                original = song
                target = os.path.join("archive/song/",name)
                shutil.copyfile(original, target)

                g = open("archive/song/yoursongpath.txt", "r+",encoding='utf-8')
                Write = True
                for i in g:                 
                    if song in i:
                        Write = False
                        break  
                g.close()  
                #write
                if Write: 
                    f = open("archive/song/yoursongpath.txt", "a",encoding='utf8')  
                    f.write(f'{target}\n')
                    f.close()
                self.box.dismiss()
            else:
                self.warning = MDDialog(                
                    type="custom",
                    title="Please choose .MP3 file",
                    buttons=[
                        MDFlatButton(
                            text="OK",
                            theme_text_color="Custom",
                            text_color = (0,0,0,1),
                            on_release = self.warningConfirm
                        ),
                    ],
                )
                self.warning.open()
            
        def warningConfirm(self,instance):
            self.warning.dismiss()

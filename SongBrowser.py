from os import name
from re import S
import re
from kivy.lang import Builder
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import BoxLayout
from kivy.uix.scatter import Scatter
from kivy.core.text import LabelBase
# Add Font
LabelBase.register(name='sf',fn_regular='archive/finalFontV2.ttf')

Builder.load_file('SongBrowser.kv')

class Browser():
    choosed = None
    class SongBrowser(BoxLayout):  
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            # self.choosed = None

        def submit(self,*args):
            Browser.choosed = args[1]
            print(f"choosed = {Browser.choosed}")
            print(f"Type = {type(Browser.choosed[0])}")

        def selected(self,filename):
            try:
                # ดูตำแหน่งไฟล์ที่เราเลือก
                Browser.choosed = filename[0]
                print(f'path = {Browser.choosed}')
            except:
                print('Error Selected')
                return

    class AddSong(MDFloatLayout):   
        def __init__(self, **kwargs):
            super(MDFloatLayout, self).__init__(**kwargs) 
            self.orientation='horizontal'
            self.size_hint=(None,None)   
            self.songbrowser = Browser().SongBrowser()
            self.box = None

        def show_songbrowser(self):
            if not self.box:
                self.box = MDDialog(                
                    type="custom",
                    content_cls=Browser().SongBrowser(),
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
            print(Browser.choosed)
            song = Browser.choosed[0]
          
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
                f.write(f'{song}\n')
                f.close()
          
            self.box.dismiss
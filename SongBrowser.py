from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import BoxLayout

Builder.load_file('SongBrowser.kv')

class SongBrowser(BoxLayout):    
    def selected(self,filename):
        try:
            print(filename[0])
        except:
            pass

class AddSong(MDFloatLayout):   
    def __init__(self, **kwargs):
        super(MDFloatLayout, self).__init__(**kwargs) 
        self.orientation='horizontal'
        self.size_hint=(None,None)   
        self.box = None

    def show_songbrowser(self):
        if not self.box:
            self.box = MDDialog(                
                type="custom",
                content_cls=SongBrowser(),
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
        self.dialog.dismiss()

    def clickConfirm(self,instance):
        pass
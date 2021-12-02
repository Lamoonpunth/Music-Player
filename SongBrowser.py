from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextField

class SongBrowser(MDFloatLayout):
    
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
        pass
    
    def clickCancel(self,instance):
        self.dialog.dismiss()

class BrowserApp(MDApp):
    def build(self):
        return AddSong()

if __name__ == '__main__':
    BrowserApp().run()
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.textfield import MDTextField
import youtube_dl
import threading

KV = '''
#:import images_path kivymd.images_path
<Content>
    orientation: "horizontal"
    size_hint_y: None
    height: "50dp"
    MDTextField:
        hint_text: "Enter Youtube URL"  
        
<DownloadURL>
    MDIconButton:
        icon: 'plus-circle-outline'
        text: "ALERT DIALOG"
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_release: root.show_enterURL()
'''

Builder.load_string(KV)
class Content(BoxLayout):
    pass

class DownloadURL(MDFloatLayout):   
    def __init__(self, **kwargs):
        super(MDFloatLayout, self).__init__(**kwargs) 
        self.orientation='horizontal'
        self.size_hint=(None,None)   
        self.dialog = None

    def show_enterURL(self):
        if not self.dialog:
            self.dialog = MDDialog(                
                type="custom",
                content_cls=Content(),
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",              
                        on_release = self.clickCancel                           
                    ),
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        on_release = self.grabText
                    ),
                ],
            )
        self.dialog.open()
    
    def clickCancel(self,instance):
        self.dialog.dismiss()

    def grabText(self, inst):
        for obj in self.dialog.content_cls.children:
            if isinstance(obj, MDTextField):
                print(obj.text)
                t2 = threading.Thread(target=self.downloadFromYoutube,args=(obj.text,), name='t2')              
                t2.start()                
        self.dialog.dismiss()

    def downloadFromYoutube(self,youtubeURL):
        video_url = youtubeURL
        video_info = youtube_dl.YoutubeDL().extract_info(
            url = video_url,download=False
        )
        filename = f"{video_info['title']}.mp3"
        
        options={
            'format':'bestaudio/best',
            'keepvideo':False,
            'outtmpl':f'archive/song/{filename}',
        }

        with youtube_dl.YoutubeDL(options) as ydl:
            ydl._ies = [ydl.get_info_extractor('Youtube')]
            ydl.download([video_info['webpage_url']])
        
        print("Download complete... {}".format(filename))   
    
        g = open("archive/song/yoursongpath.txt", "r+",encoding='utf-8')
        Write = True
        for i in g:                 
            if filename in i:
                Write = False
                break  
        g.close()      
        #write
        if Write: 
            f = open("archive/song/yoursongpath.txt", "a",encoding='utf8')  
            f.write(f'archive/song/{filename}\n')
            f.close()
            
class MainApp(MDApp):
    def build(self):
        screen = DownloadURL()
        return screen
def run():
    MainApp().run()
if __name__ == "__main__":
    t1 = threading.Thread(target=run(), name='t1')
    t1.start() 
  
    
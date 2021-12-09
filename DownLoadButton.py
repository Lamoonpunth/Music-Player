from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.textfield import MDTextField
from kivy.core.text import LabelBase
from kivymd.uix.spinner import MDSpinner

import youtube_dl
import threading
LabelBase.register(name='sf',fn_regular='archive/finalFontV2.ttf')
KV = '''
#:import images_path kivymd.images_path
<Content>    
    orientation: "horizontal"
    size_hint_y: None    
    height: "50dp"    
    MDTextField:
        hint_text: "Enter Youtube URL"  
        font_name: 'sf'
<DownloadURL>   
    size_hint_y: None      
    orientation: "horizontal"    
    
    MDIconButton:       
        id: iButton 
        icon: 'youtube'      
        pos_hint: {'center_x': .5, 'center_y': .5}
        theme_text_color: "Custom"
        on_release: root.show_enterURL()        
'''

Builder.load_string(KV)
class Content(BoxLayout):
    pass

class DownloadURL(BoxLayout):   
    def __init__(self, **kwargs):
        super(BoxLayout, self).__init__(**kwargs) 
        self.orientation='horizontal'
        self.size_hint=(None,None)   
        self.dialog = None
        self.isLoading = False 
        self.ids.iButton.text_color = (1,0,0,1.0)       
        self.spin = (MDSpinner(        
        size_hint=(None, None),
        size=(46, 46),
        pos_hint={'center_x': .5, 'center_y': .5},
        active=False,
        palette=[
            [0.28627450980392155, 0.8431372549019608, 0.596078431372549, 1],
            [0.3568627450980392, 0.3215686274509804, 0.8666666666666667, 1],
            [0.8862745098039215, 0.36470588235294116, 0.592156862745098, 1],
            [0.8784313725490196, 0.9058823529411765, 0.40784313725490196, 1],
                ]
        ))
        self.add_widget(self.spin)
    def show_enterURL(self):
        if not self.isLoading:
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
        for obj in self.dialog.content_cls.children:
            if isinstance(obj, MDTextField):
                print(obj.text)                           
                obj.text =''
        self.dialog.dismiss()

    def grabText(self, inst):
        self.spin.active = True
        self.ids.iButton.icon = ''                
        for obj in self.dialog.content_cls.children:
            if isinstance(obj, MDTextField):
                print(obj.text)
                t2 = threading.Thread(target=self.downloadFromYoutube,args=(obj.text,), name='t2')              
                t2.start()                
                obj.text =''
        self.dialog.dismiss()

    def downloadFromYoutube(self,youtubeURL):
        try:            
            self.isLoading = True
            video_url = youtubeURL
            video_info = youtube_dl.YoutubeDL().extract_info(
                url = video_url,download=False
            )
            VDname = video_info['title']
            songgpath =''
            for i in range(len(VDname)):
                if  VDname[i] not in '\/:*?"<>|':
                    songgpath += VDname[i]                    
                
            filename = f"{songgpath}.mp3"            
            options={
                'format':'bestaudio/best',
                'keepvideo':False,
                'outtmpl':f'archive/song/{filename}',
            }

            with youtube_dl.YoutubeDL(options) as ydl:
                ydl._ies = [ydl.get_info_extractor('Youtube')]
                numm = ydl.download([video_info['webpage_url']])
            
            print("Download complete... {}".format(songgpath))   
            print(f'Number: {numm}')
            self.ids.iButton.icon = 'youtube'
            self.ids.iButton.text_color = (1,0,0,1.0)
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
        except:
            print('Error')
            self.ids.iButton.icon = 'alert-box'
            self.ids.iButton.text_color = (1,1,0,1.0)
        self.isLoading = False         
        self.spin.active = self.isLoading   
class MainApp(MDApp):
    def build(self):
        screen = DownloadURL()
        return screen

def run():
    MainApp().run()
if __name__ == "__main__":
    t1 = threading.Thread(target=run(), name='t1')
    t1.start() 
  
    
from kivy import clock
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.lang.builder import Builder
from kivy.core.audio import SoundLoader
from kivy.uix.button import Button
from kivy.uix.progressbar import ProgressBar
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
import threading
from playlist import playlist
from playingqueue import playingqueue
fullpath=[]
f = open("yoursongpath.txt", "r+")
for x in f:
    if x[-1:] == "\n":
        x=x[:-1]
    fullpath.append(x)
print(fullpath)
f.close()

yoursong = playlist(fullpath)
queue = playingqueue()
print (yoursong)


#Load KV File
Builder.load_file('main.kv')

#Load Song
soundpath = "Arizona Zervas - ROXANNE (Official Video).mp3"
sound = SoundLoader.load(soundpath)

class MainGridLayout(Widget):    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.start_stop.bind(on_press=self.press)
        self.submit.bind(on_press=self.press) #สร้างปุ่มเล่น ให้ return ค่า
        self.bool = False
        thread = threading.Thread(target=self.slideRun, args=())
        thread.daemon = True 
        thread.start()
        print('Init')
           
    def slide_it(self, *args):
        sound.volume = float(args[1])/100
        print(f'Sound volume: {sound.volume}')            
        
    def seek(self, *args):
        print (f'Sound state : {sound.state}')
        print (f'Sound length: {sound.length}')
        if float(args[1])*sound.length/10000-sound.get_pos()<5 and float(args[1])*sound.length/10000-sound.get_pos()> -5:
            return 
        if (sound.state=='play'):
            print(args[1])
            sound.seek(float(args[1])*sound.length/10000)
        else:
            print(args[1])
            sound.play()
            sound.seek(float(args[1])*sound.length/10000)
            sound.stop()

    def press(self, instance):
        if self.bool is False:
            self.submit = Button(text='Play')
            self.bool = True
            print('Sound play')
            sound.play()
        else:
            self.submit = Button(text='Stop')
            self.bool = False
            print('Sound stop')            
            sound.stop()       
                              
    def slideRun(self):
        Clock.schedule_interval(lambda dt: self.playtimeUpdate(),1) #update ค่าต่างๆ
        
    def playtimeUpdate(self):
        value=int(sound.get_pos()*10000/sound.length)
        self.ids.playtime.value=value


class MainWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class MainApp(App):
    def build(self):
        return MainGridLayout()


if __name__ == "__main__":
    MainApp().run()
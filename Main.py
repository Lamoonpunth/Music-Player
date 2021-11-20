from kivy import clock
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.core.audio import SoundLoader
from kivy.uix.button import Button
from kivy.uix.progressbar import ProgressBar
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from threading import Thread
from playlist import playlist
from playingqueue import playingqueue
from song import song
from kivy.core.text import LabelBase
#Add Font
LabelBase.register(name='sf',fn_regular='archive/SF-UI-Display-Regular.ttf')
#Load KV File
Builder.load_file('main.kv')

fullpath=[]
f = open("yoursongpath.txt", "r+")
for x in f:
    if x[-1:] == "\n":
        s=song(x[:-1])
        print(s)
        fullpath.append(s)
f.close()
yoursong = playlist(fullpath)
print(yoursong)


class MainGridLayout(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.start_stop.bind(on_press=self.press)
        self.submit.bind(on_press=self.press)
        self.next.bind(on_press=self.nextpress)
        self.prev.bind(on_press=self.prevpress)
        self.bool = False
        Clock.schedule_interval(lambda dt: self.playtimeUpdate(), 0.1)
        self.queue = playingqueue()
        self.queue.chooseplaylist(yoursong)
        self.queue.addfromqueuefirstsong()
        #Load Song
        self.soundpath = self.queue.nowplaying.getpath()
        print(self.queue.nowplaying)
        self.sound = SoundLoader.load(self.soundpath)
        self.ids.song_name.text=self.queue.nowplaying.getname()
        self.ids.song_name.font_name = 'sf'
        self.volume = 0.25
    
        #seek
        self.seekvalue = 0
        self.playtimeUpdateBool = True

    def slide_it(self, *args):
        self.volume = float(args[1]/100)
        self.sound.volume = self.volume
    def valuechange(self,*args):
        self.seekvalue=args[1]
    def notupdate(self,*args):
        print("ontouchdown")
        self.playtimeUpdateBool=False
    def seek(self, *args):
        if self.playtimeUpdateBool is False:
            self.playtimeUpdateBool = True
            print("ontouchup")
            #print (sound.state)
            #print (sound.length)
            if (self.sound.state=='play'):
                print(self.seekvalue)
                self.sound.seek(self.seekvalue*self.sound.length/10000)
            else:
                self.sound.play()
                self.sound.seek(self.seekvalue*self.sound.length/10000)
                self.sound.stop()

    def press(self, instance):
            if self.bool is False:
                self.submit = Button(text='Play')
                self.bool = True
                self.sound.play()
                self.sound.volume = float(self.volume)
            else:
                self.submit = Button(text='Stop')
                self.bool = False
                self.sound.stop()
    def nextpress(self,instance):
        if self.queue.isEmpty():
            print("QueueIsEmpty")
            return
        self.sound.stop()
        self.queue.addfromqueue()
        self.soundpath = self.queue.nowplaying.getpath()
        self.sound = SoundLoader.load(self.soundpath)
        self.ids.song_name.text=self.queue.nowplaying.getname()
        self.sound.play()
        self.sound.volume = self.volume
        self.playtimeUpdate()
    def prevpress(self,instance):
        print(self.queue.isStackEmpty())
        if self.queue.isStackEmpty():
            print("StackIsEmpty")
            return
        self.sound.stop()
        self.queue.addfromstack()
        self.soundpath = self.queue.nowplaying.getpath()
        self.sound = SoundLoader.load(self.soundpath)
        self.ids.song_name.text=self.queue.nowplaying.getname()
        self.sound.play()
        self.sound.volume = self.volume
        self.playtimeUpdate()

    def playtimeUpdate(self):
        print(self.playtimeUpdateBool)
        if self.playtimeUpdateBool is True:
            #print(self.ids.playtime.value_pos)
            value=int(self.sound.get_pos()*10000/self.sound.length)
            if value>=9990:
                self.nextpress("instance")
                value=0
            self.ids.playtime.value=value
class MainWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class MainApp(App):
    def build(self):
        self.title = 'Wanwai Player'
        self.icon = 'Icon/title.png'
        return MainGridLayout()

if __name__ == "__main__":
    MainApp().run()
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
fullpath=[]
f = open("yoursongpath.txt", "r+") 
for x in f:
    if x[-1:] == "\n":
        x=x[:-1]
    fullpath.append(x)
print(fullpath)
f.close()

yoursong = playlist(fullpath)
#Load KV File
Builder.load_file('main.kv')


class MainGridLayout(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.start_stop.bind(on_press=self.press)
        self.submit.bind(on_press=self.press)
        self.next.bind(on_press=self.nextpress)
        self.prev.bind(on_press=self.prevpress)
        self.bool = False
        Clock.schedule_interval(lambda dt: self.playtimeUpdate(), 1)
        self.queue = playingqueue()
        print(yoursong)
        self.queue.chooseplaylist(yoursong)
        self.queue.addfromqueue()
        #Load Song
        self.soundpath = self.queue.nowplaying
        print(self.queue.nowplaying)
        self.sound = SoundLoader.load(self.soundpath)
        self.ids.song_name.text=self.soundpath
    def slide_it(self, *args):
        self.sound.volume = float(args[1])/100

    def seek(self, *args):
        #print (sound.state)
        #print (sound.length)
        if float(args[1]>=9990):
            self.nextpress("instance")
            return
        if float(args[1])*self.sound.length/10000-self.sound.get_pos()<5 and float(args[1])*self.sound.length/10000-self.sound.get_pos()>-5:
            return
        else:
            if (self.sound.state=='play'):
                self.sound.seek(float(args[1])*self.sound.length/10000)
            else:
                self.sound.play()
                self.sound.seek(float(args[1])*self.sound.length/10000)
                self.sound.stop()

    def press(self, instance):
            if self.bool is False:
                self.submit = Button(text='Play')
                self.bool = True
                self.sound.play()
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
        self.soundpath = self.queue.nowplaying
        self.sound = SoundLoader.load(self.soundpath)
        self.ids.song_name.text=self.soundpath
        self.sound.play()
        self.playtimeUpdate()
    def prevpress(self,instance):
        pass

    def playtimeUpdate(self):
        value=int(self.sound.get_pos()*10000/self.sound.length)
        self.ids.playtime.value=value

class MainWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class MainApp(App):
    def build(self):
        return MainGridLayout()


if __name__ == "__main__":
    MainApp().run()
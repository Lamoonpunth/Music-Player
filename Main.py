from kivy import clock
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.core.audio import SoundLoader
from kivy.uix.button import Button
from kivy.uix.progressbar import ProgressBar
from kivy.clock import Clock
#Load KV File
Builder.load_file('main.kv')
#Load Song
soundpath = "Arizona Zervas - ROXANNE (Official Video).mp3"
sound = SoundLoader.load(soundpath)

class MainGridLayout(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.start_stop.bind(on_press=self.press)
        self.submit.bind(on_press=self.press)
        self.bool = False
        Clock.schedule_interval(lambda dt: self.playtimeUpdate(), 1)

    def slide_it(self, *args):
        sound.volume = float(args[1])/100

    def seek(self, *args):
        print (sound.state)
        print (sound.length)
        if (sound.state=='play'):
            print(args[1])
            sound.seek(float(args[1])*sound.length/1000)
        else:
            pass

    def press(self, instance):
            if self.bool is False:
                self.submit = Button(text='Play')
                self.bool = True
                sound.play()
            else:
                self.submit = Button(text='Stop')
                self.bool = False
                sound.stop()

    def playtimeUpdate(self):
        value=int(sound.get_pos()*1000/sound.length)
        self.ids.playtime.value=value

class MainWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class MainApp(App):
    def build(self):
        return MainGridLayout()


if __name__ == "__main__":
    MainApp().run()
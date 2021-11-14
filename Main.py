from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.core.audio import SoundLoader
from kivy.uix.button import Button
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

    def slide_it(self, *args):
        sound.volume = float(args[1])/100

    def seek(self, *args):
        pass

    def press(self, instance):
            if self.bool is False:
                self.submit = Button(text='Play')
                self.bool = True
                sound.play()
                sound.seek(10)
                print(sound.length)
            else:
                self.submit = Button(text='Stop')
                self.bool = False
                sound.stop()

class MainWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class MainApp(App):
    def build(self):
        return MainGridLayout()


if __name__ == "__main__":
    MainApp().run()
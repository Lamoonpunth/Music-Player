from operator import truediv
from kivy.app import App
from kivy.core import text
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader
from kivy.lib.gstplayer import GstPlayer, get_gst_version
soundpath = "Arizona Zervas - ROXANNE (Official Video).mp3"

sound = SoundLoader.load(soundpath)

class MainWidget(Widget):
    pass
 
class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)
        self.rows = 2
        self.cols = 2
        self.daeng = Label(text='555+')
        self.add_widget(self.daeng)
        self.submit = Button(text='Press me senpai')
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)
        self.bool = False
        self.tony = Label(text='now playing : '+soundpath)

    def press(self, instance):
        # self.daeng.text = 'I naa hee'
        if self.bool is False:
            self.bool = True
            sound.play()
            sound.seek(10)
            print(sound.length)
        else:
            self.bool = False
            sound.stop()
            print(sound.get_pos())
        if self.bool is True:
            self.add_widget(self.tony)
        elif self.bool is False:
            self.remove_widget(self.tony)

class PongApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    app = PongApp()
    app.run()
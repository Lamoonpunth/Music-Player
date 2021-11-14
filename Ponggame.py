from sys import setprofile
from typing import Text
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader
from kivy.properties import ObjectProperty
from kivy.lang import Builder
sound = SoundLoader.load('Arizona Zervas - ROXANNE (Official Video).mp3')
#Load KV file
Builder.load_file('Pong.kv')

class MainWidget(Widget):
    def slide_it(self, *args):
        self.slide_text.text = str(int(args[1]))
        self.slide_text.font_size = str(int(args[1]))

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
        self.tony = Label(text='I naa hee')

    def press(self, instance):
        # self.daeng.text = 'I naa hee'
        if self.bool is False:
            self.bool = True
            sound.play()
        else:
            self.bool = False
            sound.stop()
        # if self.bool is True:
        #     self.add_widget(self.tony)
        # elif self.bool is False:
        #     self.remove_widget(self.tony)    

class PongApp(App):
    def build(self):
        return MainWidget()

if __name__ == '__main__':
    app = PongApp()
    app.run()
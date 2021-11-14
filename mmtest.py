#Load KV file
from sys import setprofile
from typing import Text
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from Main import MainWidget
Builder.load_file('mmtest.kv')

class mmtest(AnchorLayout):
    pass

class MyApp(App):

    def build(self):
        return mmtest()

if __name__ == '__main__':
    MyApp().run()
from os import name
from kivy.app import App
from kivy.core.text import Label
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.label import Label
from SongBox import SongBox
class SlideNorn(GridLayout):
    def __init__(self, **kwargs):
        super(SlideNorn, self).__init__(**kwargs)
        #create song from playlist
        #button
        # for i in range(5):
        #     btn = Button(text=str(i), size_hint_y=None, height=40)
        #     self.add_widget(btn)
        #label

    def spiderman(self,playlist):
        for i in range(len(playlist.playlist)):
            t = playlist.playlist[i].time
            new_t = (t//60) + ((t%60)/100)
            new_t = format(new_t,'.2f')
            time_text = f'{new_t}'
            lb = SongBox(i+1,playlist.playlist[i].name,time_text)
            self.add_widget(lb)
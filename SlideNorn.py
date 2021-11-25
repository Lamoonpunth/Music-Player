from kivy.app import App
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
class SlideNorn(BoxLayout):
    def __init__(self, **kwargs):
        super(SlideNorn, self).__init__(**kwargs)
        #create song from playlist
        for i in range(5):
            btn = Button(text=str(i), size_hint_y=None, height=40)
            self.add_widget(btn)
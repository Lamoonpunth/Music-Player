from kivy.app import App
from kivy.core import window
from kivy.core.text import Label
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color
from kivy.graphics import Rectangle
from kivymd.uix.behaviors import HoverBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.theming import ThemableBehavior
class PlaylistBox(ButtonBehavior,MDBoxLayout, ThemableBehavior, HoverBehavior):
    def __init__(self,i,name,**kwargs):
        super(PlaylistBox, self).__init__(**kwargs)
        self.orientation='horizontal'
        self.size_hint=(None,None)
        self.width = Window.width*0.19
        self.index=i
        lb=Label(size_hint_x= .1,
        text_size= (self.width,None),
        padding= (25, 10),
        text=name,
        font_name='sf',
        font_size=18,
        color=(0,0,0,1))
        self.add_widget(lb)
    def on_enter(self, *args):
        self.md_bg_color = (1, 1, 1, 1)
    def on_leave(self, *args):
        self.md_bg_color = self.theme_cls.bg_darkest
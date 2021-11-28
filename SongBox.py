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
class SongBox(ButtonBehavior,MDBoxLayout, ThemableBehavior, HoverBehavior):
    def __init__(self,i,name,time, **kwargs):
        super(SongBox, self).__init__(**kwargs)
        self.orientation='horizontal'
        self.size_hint=(None,None)
        #print(width)
        self.width=Window.width*0.7
        Window.bind(mouse_pos=self.on_maximize)
        Window.bind(mouse_pos=self.on_minimize)
        self.index=i-1
        #song number
        lb=Label(size_hint_x= .1,
        text_size= (None,None),
        padding= (25, 10),
        text=str(i),
        font_name='sf',
        font_size=18,
        color=(0,0,0,1))
        self.add_widget(lb)
        #song name
        print(f'size = {self.size}')
        lb=Label(size_hint_x= .7,
        halign= 'left',
        text_size= (0.7*self.width,None),
        padding= (25, 10),
        text=name,
        font_name='sf',
        font_size=18,
        color=(0,0,0,1))
        self.add_widget(lb)
        #time
        lb=Label(size_hint_x= .25,
        text_size= (0.2*self.width,None),
        halign='left',
        padding= (25, 10),
        text=str(time),
        font_name='sf',
        font_size=18,
        color=(0,0,0,1))
        self.add_widget(lb)
        print(self.index)
    def on_enter(self, *args):
        self.md_bg_color = (1, 1, 1, 1)
    def on_leave(self, *args):
        self.md_bg_color = self.theme_cls.bg_darkest

    # def on_touch_down(self, touch):
    #     if self.collide_point(touch.x, touch.y):
    #         self.md_bg_color = self.theme_cls.bg_darkest

    # def on_touch_up(self, touch):
    #     if self.collide_point(touch.x, touch.y):
    #         self.md_bg_color = (1, 1, 1, 1)
    def on_maximize(self,*args):
        self.width=Window.width*0.7
    def on_minimize(self,*args):
        self.width=Window.width*0.7
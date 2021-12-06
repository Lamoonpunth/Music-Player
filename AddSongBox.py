from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.behaviors import HoverBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.theming import ThemableBehavior
from kivy.core.window import Window
from kivy.uix.label import Label
class AddSongBox(ButtonBehavior,MDBoxLayout, ThemableBehavior, HoverBehavior):
    def __init__(self,**kwargs):
        super(AddSongBox, self).__init__(**kwargs)
        self.orientation='horizontal'
        self.size_hint=(None,None)             
        self.width=Window.width*0.7
        lb=Label(size_hint_x= .1,
        text_size= (None,None),
        text="+ Add Song",
        font_name='sf',
        font_size=18,
        color=(0,0,0,1)
        )
        self.add_widget(lb)

    def on_enter(self, *args):
        self.md_bg_color = (1, 1, 1, 1)
    def on_leave(self, *args):
        self.md_bg_color = self.theme_cls.bg_darkest
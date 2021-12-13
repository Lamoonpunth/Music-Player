from kivy.properties import StringProperty
from kivymd.uix.behaviors import HoverBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivymd.theming import ThemableBehavior
from kivy.uix.label import Label
from kivymd.uix.list import OneLineAvatarListItem
class PlaylistDialogBox(OneLineAvatarListItem, ThemableBehavior, HoverBehavior):
    divider = None
    source = StringProperty()
    def __init__(self,i,name,**kwargs):
        super(PlaylistDialogBox, self).__init__(**kwargs)
        self.index=i
        self.name=name
        self.text=name
        

    def on_enter(self, *args):
        self.md_bg_color = (0, 0, 0, .4)
    def on_leave(self, *args):
        self.md_bg_color = (0, 0, 0, .1)
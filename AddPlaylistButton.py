from kivymd.uix.button import MDFlatButton
from kivymd.uix.behaviors import HoverBehavior
from kivymd.theming import ThemableBehavior
class AddPlaylistButton(MDFlatButton, ThemableBehavior, HoverBehavior):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.md_bg_color = (0, 0, 0, .1)

    def on_enter(self, *args):
        self.md_bg_color = (0, 0, 0, .4)
    def on_leave(self, *args):
        self.md_bg_color = (0, 0, 0, .1)
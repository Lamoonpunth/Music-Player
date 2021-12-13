from kivymd.uix.button import MDRectangleFlatIconButton
from kivymd.uix.behaviors import HoverBehavior
from kivymd.theming import ThemableBehavior
class AddPlaylistButton(MDRectangleFlatIconButton, ThemableBehavior, HoverBehavior):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.md_bg_color = (0, 0, 0, .1)
        self.icon = 'playlist-plus'
        self.icon_color = (1,1,1,1)
        self.line_width = 0.5
        self.line_color = (1,0.41,0.69,1)
    def on_enter(self, *args):
        self.md_bg_color = (0, 0, 0, .4)
        self.icon_color = (1,0.41,0.69,1)
    def on_leave(self, *args):
        self.md_bg_color = (0, 0, 0, .1)
        self.icon_color = (1,1,1,1)
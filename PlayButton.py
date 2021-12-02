from kivymd.uix.behaviors.toggle_behavior import MDToggleButton
from kivymd.uix.button import MDIconButton
from kivymd.uix.behaviors import HoverBehavior
class PlayButton(MDIconButton,HoverBehavior):
    
    
    def on_enter(self):
        self.user_font_size= 85
        self.pos_hint = {"center_x":0.5,"center_y":0.5}
        return super().on_enter()
    def on_leave(self):
        self.user_font_size= 80
        return super().on_leave()
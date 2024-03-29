#(1,0.73,0.8,1)
from kivymd.uix.button import MDIconButton
from kivymd.uix.behaviors import HoverBehavior
from kivy.uix.behaviors import ToggleButtonBehavior
class ToggleVolumeButton(MDIconButton,HoverBehavior,ToggleButtonBehavior):

    def on_enter(self):
        if self.state is 'normal':
            self.text_color = (1,1,1,1)
        else:
            self.text_color = (1,0.60,0.75,1)           #[1,0.41,0.69,1]
        return super().on_enter()

    def on_leave(self):
        if self.state is 'normal':
            self.text_color = (0.7,0.7,0.7,1)
        else:
            self.text_color = (1,0.41,0.69,1)
        return super().on_leave()
        
    def on_release(self):
        if self.state is 'normal':
            self.text_color = (1,1,1,1)
            self.icon = 'volume-high'
        else:
            self.text_color = (1,0.60,0.75,1)
            self.icon = 'volume-mute'
        return super().on_release()
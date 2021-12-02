#(1,0.73,0.8,1)
from kivymd.uix.button import MDIconButton
from kivymd.uix.behaviors import HoverBehavior
from kivy.uix.behaviors import ToggleButtonBehavior
class ShuffleButton(MDIconButton,HoverBehavior,ToggleButtonBehavior):

    def on_enter(self):
        if self.state is 'normal':
            self.text_color = (1,1,1,1)
        else:
            self.text_color = (1,0.78,0.85,1)
        return super().on_enter()
    def on_leave(self):
        if self.state is 'normal':
            self.text_color = (0.7,0.7,0.7)
        else:
            self.text_color = (1,0.73,0.8,1)
        return super().on_leave()
    def on_release(self):
        if self.state is 'normal':
            self.text_color = (0.7,0.7,0.7)
        else:
            self.text_color = (1,0.73,0.8,1)
        return super().on_release()
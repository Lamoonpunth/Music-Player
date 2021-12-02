from kivymd.uix.button import MDIconButton
from kivymd.uix.behaviors import HoverBehavior
class NextPrevButton(MDIconButton,HoverBehavior):
    def on_enter(self):
        self.text_color=(1,1,1,1)
        return super().on_enter()
    def on_leave(self):
        self.text_color=(0.6,0.6,0.6,1)
        return super().on_leave()
    def on_press(self):
        self.text_color=(0.6,0.6,0.6,1)
        return super().on_leave()
    def on_release(self):
        self.text_color=(1,1,1,1)
        return super().on_release()
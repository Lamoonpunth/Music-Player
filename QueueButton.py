from kivymd.uix.button import MDIconButton
from kivymd.uix.behaviors import HoverBehavior
class QueueButton(MDIconButton,HoverBehavior):

    def on_enter(self):
        if self.queueshownow is True:
            self.text_color=(1,0.60,0.75,1)
        else:
            self.text_color=[1,1,1,1]
        return super().on_enter()
    def on_leave(self):
        if self.queueshownow is True:
            self.text_color = (1,0.41,0.69,1)
        else:
            self.text_color=[0.6,0.6,0.6,1]
        return super().on_leave()
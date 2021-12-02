#(1,0.73,0.8,1)
from kivymd.uix.button import MDIconButton
from kivymd.uix.behaviors import HoverBehavior
class RepeatButton(MDIconButton,HoverBehavior):
    def on_enter(self):
        if self.repeatstate == "False":
            self.text_color = (1,1,1,1)
        else:
            self.text_color = (1,0.60,0.75,1)
        return super().on_enter()
    def on_leave(self):
        if self.repeatstate == "False":
            self.text_color = (0.6,0.6,0.6)
        else:
            self.text_color = (1,0.41,0.69,1)
        return super().on_leave()
    def on_release(self):
        if self.repeatstate == "False":
            self.repeatstate = "repeatplaylist"
            self.text_color = (1,0.60,0.75,1)
        elif self.repeatstate == "repeatplaylist":
            self.repeatstate = "repeatsong"
            self.text_color = (1,0.60,0.75,1)
            self.icon = 'repeat-once'
        else:
            self.repeatstate = "False"
            self.icon = 'repeat'
            self.text_color = (1,1,1,1)
        return super().on_release()
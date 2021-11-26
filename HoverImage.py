from kivy.app import App
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.image import Image
class HoverImage(Image):
    def __init__(self, **kwargs):
        # Call the initialization function of the parent class
        super(HoverImage, self).__init__(**kwargs)
        # Set the control to fill horizontally and set the height vertically
        self.size_hint = (1, None)
        self.height = 50
        self.normalImage=""
        self.hoverImage=""
        # binding[subscribe]Event handling method of mouse position change
        Window.bind(mouse_pos=self.on_mouse_pos)
     
     # Mouse position processing method
    def on_mouse_pos(self, *args):
        # Determine whether the control is in root In root control
        if not self.get_root_window():
            return
        # Get mouse position data
        pos = args[1]
        # Check whether the mouse position is in the control
        if self.collide_point(*pos):
            # If on a control, the style method entered by the mouse is called
            Clock.schedule_once(self.mouse_enter_css, 0)
        else:
            # If on a control, the style method of mouse out is called
            Clock.schedule_once(self.mouse_leave_css, 0)
 
    def mouse_leave_css(self, *args):
        self.source=self.normalImage
 
    def mouse_enter_css(self, *args):
        self.source=self.hoverImage

    def otd(self, *args):
        self.source=self.normalImage
    def otu(self, *args):
        self.source=self.hoverImage
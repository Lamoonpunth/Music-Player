from kivy.app import App
from kivy.core import window
from kivy.core.text import Label
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color
from kivy.graphics import Rectangle
from kivymd.uix.behaviors import HoverBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.menu import MDDropdownMenu
class searchBox(ButtonBehavior,MDBoxLayout, ThemableBehavior, HoverBehavior):
    def __init__(self,i,name,time, **kwargs):
        super(searchBox, self).__init__(**kwargs)
    
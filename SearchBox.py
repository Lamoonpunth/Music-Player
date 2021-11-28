from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen

from kivymd.icon_definitions import md_icons
from kivymd.app import MDApp
from kivymd.uix.list import OneLineIconListItem
from kivy.uix.boxlayout import MDBoxLayout
from kivy.uix.label import Label

class SearchBox(MDBoxLayout):
    def __init__(self,i,name,time, **kwargs):
        super(SearchBox, self).__init__(**kwargs)             
        self.orientation = 'horizontal'
        self.spacing = .10
        self.padding = .20
        #song number
        lb=Label(size_hint_x= .1,
        text_size= (None,None),
        padding= (25, 10),
        text=str(i),
        font_name='sf',
        font_size=18,
        color=(0,0,0,1))
        self.add_widget(lb)
        #song name
        print(f'size = {self.size}')
        lb=Label(size_hint_x= .7,
        halign= 'left',
        text_size= (0.7*self.width,None),
        padding= (25, 10),
        text=name,
        font_name='sf',
        font_size=18,
        color=(0,0,0,1))
        self.add_widget(lb)
        #time
        lb=Label(size_hint_x= .2,
        text_size= (0.2*self.width,None),
        halign='left',
        padding= (25, 10),
        text=str(time),
        font_name='sf',
        font_size=18,
        color=(0,0,0,1))
        self.add_widget(lb)
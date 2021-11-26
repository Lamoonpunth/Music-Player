from kivy.app import App
from kivy.core.text import Label
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
class SongBox(BoxLayout):
    def __init__(self,i,name,width, **kwargs):
        super(SongBox, self).__init__(**kwargs)
        self.orientation='horizontal'
        self.size_hint=(None,None)
        #print(width)
        self.width=600
        #song number
        lb=Label(size_hint_x= .2,
        text_size= (None,None),
        padding= (25, 10),
        text=str(i),
        font_name='sf',
        font_size=18,
        color=(0,0,0,1))
        self.add_widget(lb)
        #song name
        lb=Label(size_hint_x= .3,
        halign= 'left',
        text_size= (None,None),
        padding= (25, 10),
        text=name,
        font_name='sf',
        font_size=18,
        color=(0,0,0,1))
        self.add_widget(lb)
        #time
        lb=Label(size_hint_x= .2,
        text_size= (None,None),
        padding= (25, 10),
        text=str(i)+":"+str(i)+str(i),
        font_name='sf',
        font_size=18,
        color=(0,0,0,1))
        self.add_widget(lb)

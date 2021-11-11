from kivy.app import App
from kivy.uix.widget import Widget

class MainApp(App):
    def build(self):
        return MainWidget()

class MainWidget(Widget):
    pass

if __name__ == "__main__":
    MainApp().run()
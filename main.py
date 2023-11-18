from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.anchorlayout import MDAnchorLayout
import webbrowser

Builder.load_file('style.kv')

class Style(MDAnchorLayout):
    pass 
    web=webbrowser 

class MainApp(MDApp):
    
    def build(self):
        self.theme_cls.theme_style='Dark'

        return Style()
    
MainApp().run()

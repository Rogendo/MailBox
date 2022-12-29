from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.scrollview import MDScrollView
from kv import KV,SPLASHSCREEN
from kivy.uix.screenmanager import ScreenManager

Window.size=(360,640)

class ContentNavigationDrawer(MDScrollView):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class MailBox(MDApp):
    def switch_theme_style(self):
        self.theme_cls.primary_palette = (
            "Orange" if self.theme_cls.primary_palette == "Red" else "Red"
        )
        self.theme_cls.theme_style = (
            "Dark" if self.theme_cls.theme_style == "Light" else "Light"
        )

    def build(self):
        # global screen_manager
        # screen_manager=ScreenManager()
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.theme_style = "Light"
        # screen_manager.add_widget(Builder.load_string(SPLASHSCREEN))
        # screen_manager.add_widget(Builder.load_string(KV))
        # return screen_manager
        return Builder.load_string(KV)

if __name__=="__main__":
    MailBox().run()
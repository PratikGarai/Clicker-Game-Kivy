from kivy.app import App
from MainMenu import MainMenu
from Game import Game
from kivy.config import Config
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label

Config.set('graphics','height',600)
Config.set('graphics','width',800)

class MainLayout(RelativeLayout):
    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
        self.LoadMenu()

    def LaunchGame(self):
        self.clear_widgets()
        self.add_widget(Game())

    def LoadMenu(self):
        self.clear_widgets()
        self.add_widget(MainMenu())

class ClickerApp(App):
    def build(self):
        return MainLayout()

if __name__=='__main__':
    ClickerApp().run()

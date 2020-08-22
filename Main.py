from kivy.app import App
from MainMenu import MainMenu
from kivy.config import Config

Config.set('graphics','height',600)
Config.set('graphics','width',800)

class ClickerApp(App):
    def build(self):
        return MainMenu()

if __name__=='__main__':
    ClickerApp().run()

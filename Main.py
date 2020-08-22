from kivy.app import App
from MainMenu import MainMenu

class ClickerApp(App):
    def build(self):
        return MainMenu()

if __name__=='__main__':
    ClickerApp().run()

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class MainMenu(FloatLayout):
    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)
        self.add_widget(Label(text='Clicker Game'))
        self.add_widget(StartButton())
        self.add_widget(QuitButton())

class StartButton(Button):
    def __init__(self,**kwargs):
        super(StartButton,self).__init__(**kwargs)
        self.text = 'Start Game'

class QuitButton(Button):
    def __init__(self,**kwargs):
        super(QuitButton,self).__init__(**kwargs)
        self.text = 'Quit Game'

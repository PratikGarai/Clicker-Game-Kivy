from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle

class MainMenu(FloatLayout):
    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)
        self.add_widget(HeadLabel())
        self.add_widget(StartButton())
        self.add_widget(QuitButton())

class HeadLabel(Label):
    def __init__(self,**kwargs):
        super(HeadLabel,self).__init__(**kwargs)
        self.pos_hint = { 'top':0.85, 'center_x':0.5 }
        self.size_hint = (0.8,0.25)
        self.text = '[b][size=50]Clicker Game[/size][size=30][/b][sub]Pratik Garai[/sub][/size]'
        self.markup = True

class StartButton(Button):
    def __init__(self,**kwargs):
        super(StartButton,self).__init__(**kwargs)
        self.pos_hint = { 'top':0.5, 'center_x':0.5 }
        self.size_hint = (0.4,0.15)
        self.text = '[b][size=30]Start Game[/size][/b]'
        self.markup = True

class QuitButton(Button):
    def __init__(self,**kwargs):
        super(QuitButton,self).__init__(**kwargs)
        self.pos_hint = { 'top':0.3, 'center_x':0.5 }
        self.size_hint = (0.4,0.15)
        self.text = '[b][size=25]Quit Game[/size][/b]'
        self.markup = True

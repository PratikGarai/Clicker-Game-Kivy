from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
import sys

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
        self.start_valid = False

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.start_valid = True
            return True
        return super(StartButton, self).on_touch_down(touch)

    def on_touch_move(self,touch):
        if self.collide_point(*touch.pos):
            self.start_valid = False
            return True
        return super(StartButton, self).on_touch_move(touch)

    def on_touch_up(self,touch):
        if self.collide_point(*touch.pos) and self.start_valid :
            self.parent.parent.LaunchGame()
            return True
        return super(StartButton, self).on_touch_up(touch)

class QuitButton(Button):
    def __init__(self,**kwargs):
        super(QuitButton,self).__init__(**kwargs)
        self.pos_hint = { 'top':0.3, 'center_x':0.5 }
        self.size_hint = (0.4,0.15)
        self.text = '[b][size=25]Quit Game[/size][/b]'
        self.markup = True
        self.quit_valid = False

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.quit_valid = True
            return True
        return super(QuitButton, self).on_touch_down(touch)

    def on_touch_move(self,touch):
        if self.collide_point(*touch.pos):
            self.quit_valid = False
            return True
        return super(QuitButton, self).on_touch_move(touch)

    def on_touch_up(self,touch):
        if self.collide_point(*touch.pos) and self.quit_valid :
            sys.exit(0)
            return True
        return super(QuitButton, self).on_touch_up(touch)

from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.properties import NumericProperty
from kivy.uix.label import Label
import random

class Block(Button):
    def __init__(self,time_to_vanish,p1,p2,**kwargs):
        super(Block, self).__init__(**kwargs)
        self.text = "Here"
        self.time_to_vanish = time_to_vanish
        self.size_hint = (0.1,0.05)
        self.pos_hint = { 'center_x':p1, 'center_y':p2 }
        Clock.schedule_once(self.vanish, self.time_to_vanish)

    def vanish(self, *args):
        try :
            self.parent.remove_widget(self)
        except :
            pass

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.parent.scored()
            self.vanish()
            return True
        return super(Block, self).on_touch_down(touch)

class ScoreBoard(Label):
    def __init__(self, **kwargs):
        super(ScoreBoard, self).__init__(**kwargs)
        self.success = 0
        self.total  = 0
        self.markup = True
        self.set_text()
        self.size_hint  = (0.2,0.1)
        self.pos_hint = { 'top':1 ,'right':1 }

    def set_text(self):
        self.text = 'Score : '+str(self.success)+'/'+str(self.total)

    def increase_success(self):
        self.success += 1
        self.set_text()

    def increase_total(self):
        self.total += 1
        self.set_text()

class BackButton(Button):
    def __init__(self, **kwargs):
        super(BackButton, self).__init__(**kwargs)
        self.text = ' < Back to Menu '
        self.size_hint= (0.2,0.1) 
        self.pos_hint = { 'top':1 ,'x':0 }

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            if self.parent.GameLoop:
                self.parent.GameLoop.cancel()
            self.parent.parent.LoadMenu()
            return True
        return super(BackButton, self).on_touch_down(touch)

class Game(RelativeLayout):

    score = NumericProperty(0)
    def __init__(self,**kwargs):
        super(Game, self).__init__(**kwargs)
        self.scoreboard = ScoreBoard()
        self.spawn_time = 0.5
        self.time_to_vanish = 1.2
        self.add_widget(self.scoreboard)
        self.add_widget(BackButton())
        self.initiate_game()
        self.GameLoop = None
    
    def scored(self):
        self.score += 1

    def on_score(self, instance, pos):
        self.scoreboard.increase_success()

    def initiate_game(self):
        self.GameLoop = Clock.schedule_interval(self.generate_block, self.spawn_time)

    def generate_block(self, *args):
        a = Block(self.time_to_vanish, random.random()*0.9+0.05, random.random()*0.85+0.025)
        self.add_widget(a)
        self.scoreboard.increase_total()

from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.properties import NumericProperty
from kivy.uix.label import Label

class Block(Button):
    def __init__(self,time_to_vanish,**kwargs):
        super(Block, self).__init__(**kwargs)
        self.text = "Here"
        self.time_to_vanish = time_to_vanish
        self.size_hint = (0.05,0.05)
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
        self.size_hint  = (0.1,0.1)
        self.pos_hint = { 'top':1 ,'right':1 }

    def set_text(self):
        self.text = str(self.success)+'/'+str(self.total)

    def increase_success(self):
        self.success += 1
        self.set_text()

    def increase_total(self):
        self.total += 1
        self.set_text()

class Game(RelativeLayout):

    score = NumericProperty(0)
    def __init__(self,**kwargs):
        super(Game, self).__init__(**kwargs)
        self.scoreboard = ScoreBoard()
        self.spawn_time = 0.8
        self.time_to_vanish = 0.4
        self.add_widget(self.scoreboard)
        self.scoreboard.set_board()
        self.initiate_game()
    
    def scored(self):
        self.score += 1

    def on_score(self, instance, pos):
        self.scoreboard.increase_success()

    def initiate_game(self):
        Clock.schedule_interval(self.generate_block, self.spawn_time)

    def generate_block(self, *args):
        a = Block(self.time_to_vanish)
        self.add_widget(a)
        self.scoreboard.increase_total()

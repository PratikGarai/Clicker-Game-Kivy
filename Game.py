from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.propties import NumericProperty
from kivy.uix.label import Label

class Block(Button):
    def __init__(self,time_to_vanish,**kwargs):
        super(Block, self).__init__(**kwargs)
        self.text = "Here"
        self.time_to_vanish = time_to_vanish
        self.size_hint = (0.05,0.05)
        Clock.schedule_once(self.vanish, self.time_to_vanish)

    def vanish(self):
        self.parent.remove(self)

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
        self.spawn_time = 0.5
        self.time_to_vanish = 1.5
        self.initiate_game()
    
    def scored(self):
        score += 1

    def on_score(self, instance, pos):
        self.scoreboard.increase()

    def initiate_game(self):
        Clock.schedule(self.generate_block(), self.spawn_time)

    def generate_block(self):
        a = Block(self.time_to_vanish)
        self.add_widget(Block)

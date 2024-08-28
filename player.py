from turtle import Turtle, Screen
from paddle import Paddles
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.player_score = 0
        self.penup()
        self.hideturtle()
        
    def increase_score(self):
        self.player_score += 1

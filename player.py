from turtle import Turtle, Screen
from paddle import Paddles
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.player_score = 0
        self.penup()
        self.hideturtle()
    paddle = Paddles()
    
    def increase_score(self):
        self.player_score += 1
   
    def move(self, player):
        for paddle in self.paddle.paddles[player]:
            paddle.forward(20)
    def move_right(self, player):
        self.setheading(90)
        self.move(player)
    def move_left(self, player):
        self.setheading(270)
        self.move(player)

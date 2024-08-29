from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()


    def move(self):
        
        x_cor = self.xcor() + 5
        y_cor = self.ycor() + 5
        self.goto(x=x_cor, y=y_cor)

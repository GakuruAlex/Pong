from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()


    def move(self):
        x_cor = self.xcor() + 10
        y_cor = self.ycor() + 10
        self.goto(x=x_cor, y=y_cor)

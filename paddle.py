from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=4)
        self.speed("fastest")
        self.penup()
        self.goto(position)
    def up(self):
        y_cor =self.ycor()
        x_cor = self.xcor() + 20
        self.goto(x=x_cor, y=y_cor)
    def down(self):
        x_cor = self.xcor()
        y_cor=self.ycor() -20
        self.goto(x=x_cor, y=y_cor)

   
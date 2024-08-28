from turtle import Turtle

class Paddles:
    def __init__(self):
        self.paddles =[]

    def add_turtle(self, position):
        for coord in position:
            turtle = Turtle()
            turtle.shape("square")
            turtle.color("white")
            turtle.speed("fastest")
            turtle.penup()
            x_cor, y_cor = coord
            turtle.goto(x=x_cor, y=y_cor)

            self.paddles.append(turtle)


    def move_one_left(self):
        for tur in self.paddles:
            tur.setheading(90)
            x_cor = tur.xcor()
            y_cor = tur.ycor() + 20
            tur.goto(x=x_cor, y=y_cor)
    def move_one_right(self):
        for tur in self.paddles[-1: : -1]:
            tur.setheading(90)
            x_cor = tur.xcor()
            y_cor = tur.ycor() - 20
            tur.goto(x=x_cor, y=y_cor)

    def move_two_left(self):
        for tur in self.paddles[-1: : -1]:
            tur.setheading(90)
            x_cor = tur.xcor()
            y_cor = tur.ycor() - 20
            tur.goto(x=x_cor, y=y_cor)
    def move_two_right(self):
        for tur in self.paddles:
            tur.setheading(90)
            x_cor = tur.xcor()
            y_cor = tur.ycor() + 20
            tur.goto(x=x_cor, y=y_cor)



from turtle import Turtle

class Paddles:
    def __init__(self):
        self.paddles =[]



    def add_turtle(self, position):
            paddle = Turtle()
            paddle.shape("square")
            paddle.color("white")
            paddle.shapesize(stretch_len=1, stretch_wid=5)
            paddle.speed("fastest")
            paddle.penup()
            x_cor, y_cor = position
            paddle.goto(x=x_cor, y=y_cor)

            self.paddles.append(paddle)


    def move_up(self):
        head = self.paddles[0]
        if head.ycor() < 243:
                x_cor = self.paddles[0].xcor()
                y_cor = self.paddles[0].ycor()
                head.goto(x =x_cor, y= y_cor + 20)

    def move_down(self):
        head = self.paddles[0]
        if head.ycor() > -240:
            x_cor = self.paddles[0].xcor()
            y_cor = self.paddles[0].ycor()
            head.goto(x =x_cor, y= y_cor - 20)
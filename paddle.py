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


    def move_up(self):
        head = self.paddles[0]
        if head.ycor() < 243:
            for i in range(len(self.paddles) - 1, 0, -1):
                x_cor = self.paddles[i].xcor()
                y_cor = self.paddles[i].ycor()
                self.paddles[i].goto(x=x_cor, y= y_cor + 20)
            head.goto(x =head.xcor(), y= head.ycor() + 20)
    def move_down(self):
        head = self.paddles[-1]
        if head.ycor() > -240:
            for i in range(0,len(self.paddles) - 1, 1):
                x_cor = self.paddles[i].xcor()
                y_cor = self.paddles[i].ycor()
                self.paddles[i].goto(x=x_cor, y= y_cor - 20)
            head.goto(x =head.xcor(), y= head.ycor() - 20)
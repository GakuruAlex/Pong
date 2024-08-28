from turtle import Turtle, Screen
class Display:
    def show_display(self)-> None:
        screen = Screen()
        screen.setup(width= 800, height = 600)
        screen.bgcolor("black")
        screen.title("Pong Game")
        #Turtle
        divide_screen = Turtle()
        divide_screen.color("white")
        divide_screen.penup()
        divide_screen.hideturtle()
        divide_screen.speed()
        divide_screen.goto(0, 290)
        divide_screen.setheading(270)
        divide_screen.pensize(5)
        for i in range(290, -285, -15):
            if i % 10 == 0:
                divide_screen.pendown()
                divide_screen.forward(15)
            else:
                divide_screen.penup()
                divide_screen.forward(15)


        screen.exitonclick()

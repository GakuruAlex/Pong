from turtle import Turtle, Screen
from paddle import Paddles
from player import Player
from ball import Ball
STARTING_POSITION ={
    "player_one": [(-390,-20), (-390, 0), (-390, 20)],
    "player_two": [(390, -20), (390, 0), (390, 20)]
}
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
        #Create paddles
        paddle_one = Paddles()
        paddle_two =Paddles()
        paddle_one.add_turtle(STARTING_POSITION["player_one"])
        paddle_two.add_turtle(STARTING_POSITION["player_two"])

        screen.listen()
        screen.onkey(paddle_one.move_up,"w")
        screen.onkey(paddle_one.move_down, "s")
        screen.onkey(paddle_two.move_down, "Down")
        screen.onkey(paddle_two.move_up, "Up")




        screen.exitonclick()

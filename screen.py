from turtle import Turtle, Screen
from paddle import Paddles
from player import Player
FONT = ('Arial', 14, 'normal')
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
        paddles = Paddles()
        #Create players
        player_one = Player()
        player_two = Player()
        player_one.goto(-280, 280)
        player_two.goto(20, 280)
        player_one.write(f"Player One Score: {player_one.player_score}", font=FONT)
        player_two.write(f"Player Two Score: {player_two.player_score}", font=FONT)
        screen.onkey()


        screen.exitonclick()

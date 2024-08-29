from screen import Display
from turtle import Screen
from paddle import Paddles
STARTING_POSITION ={
    "player_one": (-390, 0),
    "player_two": (390, 0)
}

def main()->None:
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(width=800, height= 600)
    screen.title("Pong Game")


    screen.exitonclick()

from turtle import Screen
from paddle import Paddle
STARTING_POSITION ={
    "player_one": (-390, 0),
    "player_two": (390, 0)
}

def main()->None:
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(width=800, height= 600)
    screen.title("Pong Game")
    
    left_paddle = Paddle(STARTING_POSITION["player_one"])
    right_paddle = Paddle(STARTING_POSITION["player_two"])

    screen.listen()

    screen.onkey(left_paddle.up, "w")
    screen.onkey(left_paddle.down, "s")
    screen.onkey(right_paddle.up, "Up")
    screen.onkey(right_paddle.down, "Down")




    screen.update()
    screen.exitonclick()

if __name__=="__main__":
    main()
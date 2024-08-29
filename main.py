
import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from player import Player
STARTING_POSITION ={
    "player_one": (-370, 0),
    "player_two": (370, 0)
}

def main()->None:
    game_is_on = True
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(width=800, height= 600)
    screen.title("Pong Game")
    player_one = Player((-50,270))
    player_two = Player((50, 270))
    
    
    left_paddle = Paddle(STARTING_POSITION["player_one"])
    right_paddle = Paddle(STARTING_POSITION["player_two"])
    ball = Ball()

    screen.listen()

    screen.onkey(left_paddle.up, "w")
    screen.onkey(left_paddle.down, "s")
    screen.onkey(right_paddle.up, "Up")
    screen.onkey(right_paddle.down, "Down")

    while game_is_on:
        time.sleep(0.1)

        ball.move()
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()
        if ball.distance(right_paddle) < 40 and ball.xcor() > 350 or ball.distance(left_paddle) < 40 and ball.xcor() < -350:
            ball.bounce_x()
        if ball.xcor() > 370:
            player_one.increase_r_score()
            ball.reset_position()
        if ball.xcor() < -370:
            player_two.increase_l_score()
            ball.reset_position()



    screen.exitonclick()

if __name__=="__main__":
    main()
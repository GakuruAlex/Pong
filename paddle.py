from turtle import Turtle
STARTING_POSITION ={
    "player_one": [(-390,-20), (-390, 0), (-390, 20)],
    "player_two": [(390, -20), (390, 0), (390, 20)]
}
class Paddles:
    def __init__(self):
        self.paddles = {"player_one":[], "player_two": []}
        self.set_paddle()




    def add_turtle(self,player, position):
        for coord in position:
            turtle = Turtle()
            turtle.shape("square")
            turtle.color("white")
            turtle.speed("fastest")
            turtle.penup()
            x_cor, y_cor = coord
            turtle.goto(x=x_cor, y=y_cor)

            self.paddles[player].append(turtle)


    def set_paddle(self):
        for player,position in STARTING_POSITION.items():
            self.add_turtle(player, position)

    def one_move_left(self):

        for tur in self.paddles["player_one"]:
            tur.setheading(90)
            x_cor = tur.xcor()
            y_cor = tur.ycor() + 20
            tur.goto(x=x_cor, y=y_cor)
    def move_one_right(self):
        for tur in self.paddles["player_one"][-1: : -1]:
            tur.setheading(90)
            x_cor = tur.xcor()
            y_cor = tur.ycor() - 20
            tur.goto(x=x_cor, y=y_cor)



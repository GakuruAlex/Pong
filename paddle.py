from turtle import Turtle
STARTING_POSITION ={
    "player_one": [(-390,-20), (-390, 0), (-390, 20)],
    "player_two": [(390, -20), (390, 0), (390, 20)]
}
class Paddles:
    def __init__(self):
        self.paddles = {"player_one":[], "player_two": []}
        self.set_paddle()
        self.player_one_head = self.paddles["player_one"][0]
        self.player_two_head = self.paddles["player_two"][0]
        self.move_paddle("player_one")



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

   

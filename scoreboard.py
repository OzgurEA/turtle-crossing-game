
from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.which_level = 1
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 260)
        self.write(f"Level: {self.which_level}", False, "center", FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f'Game is Over. Your score is: {self.which_level}', False, "center", FONT)


    def level_uping(self):
        self.which_level += 1
        self.update_scoreboard()




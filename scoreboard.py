from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.hideturtle()
        self.penup()
        self.shapesize(stretch_wid=.5, stretch_len=.5)
        self.color('white')
        self.update_board(0)

    def update_board(self, i):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score {i}", False, ALIGNMENT, FONT)

    def game_over(self):
        self.home()
        self.write("Game Over", False, "center", FONT)

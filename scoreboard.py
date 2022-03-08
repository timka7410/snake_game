from turtle import Turtle
Aligment = "center"
FONT = ('Courier', 22, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super(Scoreboard, self).__init__()
        self.score = 0
        self.write_score()
        self.hideturtle()

    def scoure_up(self):
        self.score += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(0, 265)
        self.color("white")
        self.write(f"Score: {self.score}", align=Aligment, font=FONT)

    def game_over(self):
        self.goto(0, 150)
        self.color("white")
        self.write(f"GAME OVER", align=Aligment, font=FONT)



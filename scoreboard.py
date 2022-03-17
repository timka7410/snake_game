from turtle import Turtle
Aligment = "center"
FONT = ('Courier', 22, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super(Scoreboard, self).__init__()
        self.score = 0
        # self.high_score = 0
        with open("data.txt") as highscore_data:
            self.high_score = int(highscore_data.read())
        self.write_score()
        self.hideturtle()

    def scoure_up(self):
        self.score += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(0, 265)
        self.color("white")
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=Aligment, font=FONT)

    # def game_over(self):
    #     self.goto(0, 150)
    #     self.color("white")
    #     self.write(f"GAME OVER", align=Aligment, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", mode="w") as highscore_data:
                highscore_data.write(str(self.score))
            self.high_score = self.score
        self.score = 0
        self.write_score()
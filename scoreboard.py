from turtle import Turtle
FONT = ('Courier', 25, 'bold')
SCORE = 0
ALIGN = "center"

class Scoreboard(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.score = SCORE
        self.create_score(x, y)

    def create_score(self, x, y):
        self.goto(x=x, y=y)
        self.penup()
        self.hideturtle()
        self.color("white")
        self.write(f"{self.score}", align=ALIGN, font=FONT)

    def inc_score(self):
        self.clear()
        self.score += 1
        self.write(f"{self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(f"GAME OVER!",align='center', font=FONT)

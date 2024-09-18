from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.create_seg(x, y)

    def create_seg(self, x, y):
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.goto(x, y)

    def Up(self):
        if self.ycor() < 250:
            y = self.ycor() + 20
            self.goto(x=self.xcor(), y=y)

    def Down(self):
        if self.ycor() > -250:
            y = self.ycor() - 20
            self.goto(x=self.xcor(), y=y)

















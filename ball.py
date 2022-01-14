from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        # self.goto(-200,0)
        self.xm = 10
        self.ym = 10
        self.sd = 0.1
    def mv(self):
        nx = self.xcor() + self.xm
        ny = self.ycor() + self.ym
        self.goto(nx, ny)
    def bncy(self):
        self.ym *= -1
        self.sd *= 0.9
    def bncx(self):
        self.xm *= -1
        self.sd *= 0.9
    def rst(self):
        self.goto(0, 0)
        self.sd = 0.1
        self.bncx()


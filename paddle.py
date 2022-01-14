from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,ps):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(ps)
    def crl(self):
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0,0)


    def gop(self):
        ny1 = self.ycor() + 20
        self.goto(self.xcor(), ny1)

    def god(self):
        ny2 = self.ycor() - 20
        self.goto(self.xcor(), ny2)


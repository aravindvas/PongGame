from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.ls = 0
        self.rs = 0
        self.ups()

    def ups(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.ls, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.rs, align="center", font=("Courier", 80, "normal"))

    def lp(self):
        self.ls += 1
        self.ups()
    def rp(self):
        self.rs += 1
        self.ups()


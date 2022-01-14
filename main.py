import turtle as t

from ball import Ball
from paddle import Paddle
import time
from score import Score


s = t.Screen()
s.title("Aravind's Pong")
s.bgcolor("black")
s.setup(width=800,height=600)
s.tracer(0)

lp = Paddle((-350,0))
rp = Paddle((350,0))
bl = Ball()
sb = Score()


s.listen()
s.onkey(rp.gop, "Up")
s.onkey(rp.god, "Down")
s.onkey(lp.gop, "w")
s.onkey(lp.god, "s")
end = False
while not end:
    time.sleep(bl.sd)
    s.update()
    bl.mv()
    if bl.ycor() > 280 or bl.ycor() < -280 :
        bl.bncy()
    if bl.distance(rp) < 50 and bl.xcor() > 320 or bl.distance(lp) < 50 and bl.xcor() < -320 :
        bl.bncx()
    if bl.xcor() > 395 :
        bl.rst()
        sb.lp()
    if bl.xcor() < -395 :
        bl.rst()
        sb.rp()



s.exitonclick()
from turtle import *
from random import *

shape("turtle")
color("green")
goto(-300, 0)
down()
goto(300, 0)

target = randint(50, 150)
pensize(3)
color("red")
up()
goto(target - 25, 2)
down()
goto(target +25, 2)

r = Turtle()
screen=Screen()
screen.addshape("rabbit.gif")
r.shape("rabbit.gif")
r.up()
r.goto(target-5, 30)

color("orange")
up()
goto(-200, 10)
setheading(20)

from turtle import *

shape("turtle")
color("orange")
speed(8)
penup()
goto(-200,200)

for step in range(20):
    rt(90)
    fd(10)
    pendown()
    fd(130)
    penup()
    bk(140)
    lt(90)
    fd(25)

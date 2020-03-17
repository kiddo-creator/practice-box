from turtle import *
from random import randint

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

goto(0,-55)
pendown()
fd(50)
lt(90)
fd(20)
lt(90)
fd(100)
lt(90)
fd(20)
lt(90)
fd(50)

a = Turtle()
screen=Screen()
screen.addshape("mouse.gif")
a.shape("mouse.gif")
a.penup()
a.goto(0, 250)

t1=Turtle()
t1.color('red')
t1.shape('turtle')
t1.penup()
t1.goto(-220,170)
t1.pendown()

t2=Turtle()
t2.color('yellow')
t2.shape('turtle')
t2.penup()
t2.goto(-220,140)
t2.pendown()

t3=Turtle()
t3.color('blue')
t3.shape('turtle')
t3.penup()
t3.goto(-220,110)
t3.pendown()

t4=Turtle()
t4.color('green')
t4.shape('turtle')
t4.penup()
t4.goto(-220, 80)
t4.pendown()


n = textinput("선택", "응원할 거북이를 선택해 주세요")
a.color("red")
a.write(n + "번 이겨라!         ", left)

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


ad1=0
ad2=0
ad3=0
ad4=0


n = textinput("선택", "응원할 거북이를 선택해주세요")
a.color("red")
a.write(n + "번 이겨라!       ", right)


for turn in range(180):
    r1=randint(1,5)
    r2=randint(1,5)
    r3=randint(1,5)
    r4=randint(1,5)
    t1.fd(r1)
    t2.fd(r2)
    t3.fd(r3)
    t4.fd(r4)
    ad1+=r1
    ad2+=r2
    ad3+=r3
    ad4 += r4


    if ad1>=500:
        t1.goto(0,10)
        t1.write("      1번 거북이 우승!")
        break
    elif ad2>=500:
        t2.goto(0,10)
        t2.write("      2번 거북이 우승!")
        break
    elif ad3>=500:
        t3.goto(0,10)
        t3.write("      3번 거북이 우승!")
        break
    elif ad4>=500:
        t4.goto(0,10)
        t4.write("      4번 거북이 우승!")
        break

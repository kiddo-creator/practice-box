from turtle import *
import random
import winsound

def turn_up():
   lt(2)

def turn_down():
   rt(2)

def fire():
  ang = heading()
  while ycor() > 0:
    forward(15)
    rt(5)

  d = distance(target, 0)
  sety(random.randint(10, 100))
  if d < 25:
    color("blue")
    write("아얏!", False, "center", ("", 15))
    winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
  else:
    color("red")
    write("메롱^^", False, "center", ("", 15))
    winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
  color("orange")
  goto(-200, 10)
  setheading(ang)

shape("turtle")
color("green")
goto(-300, 0)
down()
goto(300, 0)

target = random.randint(50, 150)
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
setheading(30)

onkeypress(turn_up, "Up")
onkeypress(turn_down, "Down")
onkeypress(fire, "space")
listen()
mainloop()

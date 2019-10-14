import turtle
import random

turtle.title("거북이 대포 게임 ver. 비특코인")

t = turtle.Turtle()
t.hideturtle()
t.up()

t.goto(70,-90)
t.write("거북이 대포 게임", font=("함초롬바탕", 80, "bold"), align="center")

t.goto(120,-150)
t.write("잠시후 실행됩니다...", font=("함초롬바탕", 40, "normal"), align="center")

t.goto(950,-500)
t.write("코드 제작: 이승찬, '모두의 파이썬' / 코드 편집: 비특코인", font=("함초롬바탕", 10, "normal"), align="right")

t.clear()

import turtle as t
import random
import os
t.shape("turtle")

def turn_up():
  t.left(2)

def turn_down():
  t. right(2)

def fire():
  ang = t.heading()
  while t.ycor()>0:
    t.forward(15)
    t. right(5)

  d = t.distance(target,0)
  t.sety(random.randint(10, 100))
  if d < 15:
    def gogo():
      t.goto(-200,10)
      t.ontimer(t.color("green") | t.write("Perfect!" , False, "center" | ("", 15)), 3/1000)
      t.setheading(ang)


  elif d < 25:
    t.color("blue")
    t.write("Great!", False, "center", ("", 15))
    t.goto(-200,10)
    t.ontimer(clear, 3/1000)
    t.setheading(ang)


  elif d < 40:
    t.color("purple")
    t.write(ontimer "Good!", False, "center", ("", 15))
    t.goto(-200,10)
    t.ontimer(clear, 3/1000)
    t.setheading(ang)

  else:
    t.color("red")
    t.write("Bad!", False, "center", ("", 15))
    t.goto(-200,10)
    t.ontimer(clear, 3/1000)
    t.setheading(ang)

  
t.goto(-300,0)
t.down()
t.goto(300,0)

target = random.randint(50,150)
t.pensize(10)
t.color("green")
t.up()
t.goto(target - 25, 2)
t.down()
t.goto(target + 25, 2)

t.color("black")
t.up()
t.goto(-200 , 10)
t.setheading(20)

t.onkeypress(turn_up, "Up")
t.onkeypress(turn_down, "Down")
t.onkeypress(fire, "space")



t.listen()

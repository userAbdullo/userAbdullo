from turtle import *
import colorsys as cs
from random import uniform
a=Screen()
a.title("turtle2")
hideturtle()
bgcolor("black")
pensize(10)
width(10)
speed(0)
for i in range(360):
    color(cs.hsv_to_rgb(i/45,uniform(0,1),1))
    pensize(2)
    forward(150)
    right(30)
    forward(60)
    left(90)
    forward(60)
    right(60)
    penup()
    setposition(0,0)
    pendown()
    right(1)
done()
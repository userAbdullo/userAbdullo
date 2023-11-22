from turtle import *
import colorsys as cs
a=Screen()
a.title("turtle4")
hideturtle()
speed(1)
setup(800,800)
tracer(10)
width(4)
bgcolor("black")
def square(x):
    for i in range(3):
        forward(x)
        left(90)
    forward(x)
for j in range(20):
    for i in range(10):
        color(cs.hsv_to_rgb(i/10,1-j/20,1))
        right(135)
        square(200-j*4)
        right(135)
        circle(50,36)

done()

from turtle import *
import colorsys as cs
a=Screen()
a.title("turtle5")
hideturtle()
speed(0)
h=0
bgcolor("black")
for i in range(16):
    for j in range(18):
        c=cs.hsv_to_rgb(h,1,1)
        color(c)
        h+=0.005
        rt(90)
        circle(150-j*6,90)
        lt(90)
        circle(150-j*6,90)
        rt(180)
    circle(40,24)
done()
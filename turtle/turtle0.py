import turtle as tur
a=tur.Screen()
a.title("turtle1")
tur.hideturtle()
tur.bgcolor("black")
tur.pencolor("red")
tur.pensize(8)
tur.up()
tur.goto(-200,0)
tur.down()
for i in range(10):
    tur.forward(400)
    tur.right(200)

tur.done()

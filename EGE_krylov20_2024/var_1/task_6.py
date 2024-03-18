from turtle import *
tracer(0)
left(90)

screensize(3000, 3000)
m = 20

down()
for i in range(2):
    forward(17 * m)
    left(90)
    forward(10 * m)
    left(90)

up()
backward(4 * m)
right(90)
backward(3 * m)
left(90)

down()
for i in range(2):
    forward(40 * m)
    right(90)
    forward(10 * m)
    right(90)

up()
for x in range(-40, 40):
    for y in range(-40, 40):
        setpos(x * m, y * m)
        dot(4)

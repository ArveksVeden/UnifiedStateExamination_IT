from turtle import *
tracer(0)

screensize(2000, 2000)
m = 30

left(90)
down()

for i in range(2):
    forward(15 * m)
    left(90)
    forward(20 * m)
    left(90)
up()
right(90)
backward(7 * m)
left(90)
forward(9)
down()
for i in range(2):
    forward(17 * m)
    right(90)
    forward(15 * m)
    right(90)
up()
for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x * m, y * m)
        dot(4, 'blue')

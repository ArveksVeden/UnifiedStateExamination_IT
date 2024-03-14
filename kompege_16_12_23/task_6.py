from turtle import *
tracer(0)

m = 40
screensize(2000, 2000)
left(90)

for i in range(2):
    forward(5 * m)
    left(90)
    backward(13 * m)
    left(90)

up()
backward(10 * m)
right(90)
forward(9 * m)
left(90)
down()

for i in range(2):
    forward(11 * m)
    right(90)
    forward(7 * m)
    right(90)

up()
for x in range(-30, 30):
    for y in range(-30, 30):
        setpos(x * m, y * m)
        dot(6, 'red')

done()
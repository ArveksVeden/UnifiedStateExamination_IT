from turtle import *
tracer(0)
left(90)

screensize(-100, 100)

m = 50

right(60)
forward(4 * m)
right(120)
for i in range(4):
    forward(3 * m)
    right(240)
    forward(3 * m)
    right(120)
forward(4 * m)
right(90)
forward(8*3**0.5 * m)
right(90)
forward(8 * m)

up()
for x in range(-30, 30):
    for y in range(-30, 30):
        setpos(x * m, y * m)
        dot(6, 'red')
done()
"""Draw a series of spiral and geometric patterns using the turtle graphics module."""
import turtle

turtle.forward(150)
turtle.right(250)
turtle.forward(150)
turtle.circle(200)
turtle.forward(50)
turtle.speed(140)
while True:
    turtle.left(50)
    turtle.forward(50)
    count = 0
    count+=1
    if count == 30:
        break
i = 1
turtle.speed(200)
while True:
    turtle.left(i)
    turtle.forward(i)
    i += 1

    if i == 200:
        break
turtle.speed(140)
i = 1
while True:
    turtle.forward(i)
    turtle.left(i)
    turtle.back(i)
    i += 1
    if i == 300:
        break

turtle.done()

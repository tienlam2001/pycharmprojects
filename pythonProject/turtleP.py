import turtle
from turtle import Turtle, Screen
turtle = Turtle()
turtle.shape("turtle")

turtle.color("red")
x = 3
for loop in range(8):
    angle = 360 / x
    for loop2 in range(x):
        turtle.forward(100)
        turtle.right(angle)

    x += 1



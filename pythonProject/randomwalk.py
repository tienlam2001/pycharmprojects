from turtle import Turtle, Screen
import random
drawer = Turtle()

arrayRandome = [0,90,180,270]
screen = Screen()
screen.colormode(255)
widthSize = 5
drawer.width(widthSize)
drawer.speed("fastest")

for i in range(100):
    widthSize += 0.03
    red = random.uniform(0, 255)
    green = random.uniform(0, 255)
    blue = random.uniform(0, 255)
    randomMove = random.randint(0,3)
    drawer.pencolor((round(red),round(green),round(blue)))
    drawer.setheading(arrayRandome[randomMove])
    drawer.forward(20)
    drawer.width(widthSize)

direction = []


screen.exitonclick()

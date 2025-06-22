import turtle
import math

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)
t.pensize(2)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(450):
    t.pencolor(colors[i % len(colors)])  # Cycle through colors
    t.forward(math.sqrt(i) * 10)  # Grow in size
    t.right(91)  # Creates the spiral effect

turtle.done()

import turtle
import math

bob = turtle.Turtle()
bob.color("red","yellow")
bob.speed(10)  # how quick it can do

#bob.begin_fill()
for i in range(50):
    bob.forward(200)
    bob.left(170)

#bob.end_fill()

turtle.done()
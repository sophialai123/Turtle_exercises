import turtle
from turtle import Turtle,Screen
import random

timmy = Turtle()

# draw a square:
# for i in range(4):
#     timmy.forward(100)
#     timmy.left(90)


# draw a dash line:

# for i in range(20):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(5)
#     timmy.pendown()

# Draw a triangle

# timmy.getscreen().bgcolor("skyblue")
# for _ in range(3):
#     timmy.right(120)
#     timmy.forward(100)
#
#
#
# for _ in range(5):
#     timmy.right(72)
#     timmy.forward(100)

'''   
# draw a different shapes at once 
colors = ["violet", "plum", "dark salmon", "orchid", "cornflower blue", "deep sky blue", "khaki","pink","DarkOrchid",
"LightSeaGreen","wheat", "SlateGray", "SeaGreen"]
def shapes(num_sides):
    angle = 360 / num_sides
    for x in range(num_sides):
        timmy.forward(100)
        timmy.right(angle) # 向下走， 向上的话： turn lef。


for i in range(3, 11):
    timmy.color(random.choice(colors)) # to get a random color
    shapes(i)

'''

""" 
random walk 
colors = ["violet", "plum", "dark salmon", "orchid", "cornflower blue", "deep sky blue", "khaki","pink","DarkOrchid",
 "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
timmy.speed(10)
timmy.pensize(10)
#angle = random.randint(-90, 90)

distances = [0, 90, 180, 270]

for x in range(200):
    timmy.color(random.choice(colors))
    timmy.forward(30)
    timmy.setheading(random.choice(distances)
"""

# how to generator a random color :
turtle.colormode(255)
def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r ,g ,b)
    return color

timmy.speed(10)


# draw a spirograph
# for i in range(100):
#     timmy.color(random_colors())
#     timmy.circle(100)
#     timmy.right(10)

# draw a spirograph solution from udemy:
timmy.speed(10)
def draw_spirograph(shape_size):
    for i in range(int(360 / shape_size)):
        timmy.color(random_colors())
        timmy.circle(100)

        timmy.setheading(timmy.heading() + shape_size)

print(draw_spirograph(5))

turtle.done()


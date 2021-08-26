import random

import colorgram
import turtle as turtle_module  # name as a variable
""" 
how to extract colors from the image:
colors = colorgram.extract('image.jpg', 30)
rgb_list = []


for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_colors = (r,g,b)
    rgb_list.append(new_colors)

print(rgb_list)

"""

# draw 100 dots
tim =turtle_module.Turtle()
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
turtle_module.colormode(255) # to get rgb color
color_list = [(231, 251, 242), (198, 12, 32), (250, 237, 17), (39, 77, 189), (38, 217, 67), (238, 228, 5),
              (229, 159, 46), (27, 39, 158), (215, 74, 12), (15, 154, 16), (199, 14, 10), (242, 247, 252),
              (244, 33, 165), (229, 17, 122), (73, 9, 31), (60, 14, 8), (224, 141, 211), (222, 160, 8), (10, 98, 61),
              (17, 18, 43), (47, 214, 232), (11, 227, 239), (79, 72, 215), (237, 155, 222), (73, 213, 169),
           (78, 234, 201), (50, 234, 244), (3, 66, 40)]

tim.hideturtle()
num_of_dots = 100
tim.speed("fastest")
for dot_count in range(1, num_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
screen = turtle_module.Screen()
screen.exitonclick() # the screen will not disappear until you click it.

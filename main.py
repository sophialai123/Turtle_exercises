import turtle
""" 
Square shape: 
 
bob = turtle.Turtle() # you can choose a variable name
bob.color("red","blue") # red is outside , blue is filled color.

bob.begin_fill() # begin fill and end fill together
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.end_fill() # end fill color

"""

bob = turtle.Turtle()
bob.color("red","blue")

bob.begin_fill()
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)

bob.penup()
bob.forward(150)
bob.pendown()


bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.end_fill()









turtle.done()
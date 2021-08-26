import turtle


star = turtle.Turtle()
star.getscreen().bgcolor("#994444")
star.speed(10)
# for i in range(5):
#     star.forward(100)
#     star.left(216)
# a star
star.penup()
star.goto(-200,100)
star.pendown()

def stars(turtle,size):
    if size <= 10:
        return
    else:
        turtle.begin_fill()
        for i in range(5):
            turtle.forward(size)
            stars(turtle, size / 3)
            turtle.left(216)
        turtle.end_fill()

stars(star,360)

turtle.done()
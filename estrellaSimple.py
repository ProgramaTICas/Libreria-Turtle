import turtle


def estrellaSimple():
    star = turtle.Turtle()
    for i in range(6):
        star.forward(50)
        star.right(144)
    turtle.done()


estrellaSimple()
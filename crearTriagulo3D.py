
import turtle


def crearLineas():
    pintor = turtle.Turtle()
    pintor.pencolor("blue")

    for i in range(50):
        pintor.forward(50)
        pintor.left(123)

    pintor.pencolor("red")
    for e in range(50):
        pintor.forward(100)
        pintor.left(123)

    turtle.done()

crearLineas()









import turtle

def espora():
    esporaDibujo = turtle.Turtle()
    esporaDibujo.pencolor("pink")
    esporaDibujo.speed(5)

    for i in range(180):
        esporaDibujo.forward(100)
        esporaDibujo.right(30)
        esporaDibujo.forward(20)
        esporaDibujo.left(60)
        esporaDibujo.forward(50)
        esporaDibujo.right(30)

        esporaDibujo.penup()
        esporaDibujo.setposition(0, 0)
        esporaDibujo.pendown()

        esporaDibujo.right(2)
    turtle.done()


espora()
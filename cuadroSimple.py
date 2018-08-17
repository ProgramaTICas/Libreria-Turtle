import turtle


def cuadro():
    smart = turtle.Turtle()
    for i in range(4): # el 4 simboliza la cantidad de lineas que dibujara para formar el cuadrado
        smart.forward(50) # rango en el cual la flecha abarcara
        smart.right(90) # indica la cantidad de veces que se va mover a la derecha
    turtle.done() #permite un stop al finalizar el dibujo


cuadro()
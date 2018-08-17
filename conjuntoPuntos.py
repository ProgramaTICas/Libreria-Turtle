import turtle

def conjuntoPuntos():
    seurat = turtle.Turtle()
    distanciaDePuntos = 25
    puntosAncho = 7
    cantPuntosAlto = 4

    seurat.penup()

    for y in range(cantPuntosAlto):
        for i in range(puntosAncho):
            seurat.dot()
            seurat.forward(distanciaDePuntos)
            seurat.pencolor("orange")
        seurat.backward(distanciaDePuntos * puntosAncho)
        seurat.right(90)
        seurat.forward(distanciaDePuntos)
        seurat.left(90)

    turtle.done()

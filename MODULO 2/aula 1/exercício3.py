listaA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listaB = []
for numero in listaA:
    if numero < 2 and numero % numero == 0:
        listaB.append(numero)
        
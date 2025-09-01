listaA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listaB = []
for numero in listaA:
    if numero < 2:
        continue
    primo = True
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
            break
    if primo:
        listaB.append(numero)
print(f'Os números primos são {listaB}')

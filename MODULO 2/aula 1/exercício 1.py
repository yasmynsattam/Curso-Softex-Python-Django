# CONTANDO QUANTAS VEZES UM NÚMERO APARECE NA LISTA

numeros = [1, 5, 2, 8, 5, 3, 5]
contador = 0
numero_procurado = 5

for numero in numeros:
    if numero == numero_procurado:
        contador += 1

print(f"O número {numero_procurado} aparece {contador} vezes na lista.")
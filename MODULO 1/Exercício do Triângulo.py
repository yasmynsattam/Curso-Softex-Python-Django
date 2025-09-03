#exercício de triângulo
lA = input("Digite o valor do lado A: ")
lB = input("Digite o valor do lado B: ")
lC = input("Digite o valor do lado C: ")

if lA.isdigit() and lB.isdigit() and lC.isdigit():
    lA = int(lA)
    lB = int(lB)
    lC = int(lC)

    if lA > 0 and lB > 0 and lC > 0:
        if (lA < lB + lC) and (lB < lA + lC) and (lC < lA + lB):
            if (lA > abs(lB - lC)) and (lB > abs(lA - lC)) and (lC > abs(lA - lB)):
                print("Os valores podem forma um triângulo")
            else: 
                print("Os valores não podem formar um triângulo")
        else: 
            print("Os valores não podem formar um triângulo")
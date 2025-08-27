

formato = "(XX)XXXXX-XXXX"
telefone = (input("Digite um número de telefone com 11 dígitos: "))
if len(telefone) != 11:
    print("É necessário que o número tenha 11 dígitos")
elif not telefone.isdigit():
    print("não é possível gerar números de telefone com esses valores")
else:
    valido = True
    for c in telefone: 
        contador = 0 
        for d in telefone:
            if d == c:
                contador += 1
        if contador >= 3:
            valido = False 
            break 

    if not valido: 
        print("Não é possível gerar um número de telefone com esses valores")
    else: 
        print(
            "("
            + telefone[0]  
            + telefone[1]
            +")" 
            + telefone[2] 
            + telefone[3] 
            + telefone[4] 
            + telefone[5] 
            + telefone[6] 
            + telefone[7] 
            + telefone[8] 
            + telefone[9] 
            + telefone[10])
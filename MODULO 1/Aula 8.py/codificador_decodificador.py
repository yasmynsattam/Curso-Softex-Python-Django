frase = input("Digite uma frase: ")
codificacao = frase.replace("a", "1").replace("e", "2").replace("i", "3").replace("o", "4").replace("u", "5")
print(f"Sua frase codificada {codificacao}")
print(f"Sua frase decodificada {frase}")
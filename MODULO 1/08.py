Palavra = input("digite uma palavra:")
letra = input("digite uma letra")
if letra in Palavra:
    print(f"A letra '{letra}'está na palavra '{Palavra}'.")
else: 
    print(f"A letra '{letra}' não está na palavra '{Palavra}'.")

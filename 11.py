usuario = input("Digite um usuário:")
senha = input (" Digite uma senha:")
if ("admin" in usuario) and (len(senha)<0):
    print("acesso permitido")

#Desafio: Análise de Dados de Acessos#

registros = []
usuarios_sucesso = set()
tempo = 0

while True:
    usuario = input("Digite o nome de usuário ou 'sair': ").lower()
    if usuario == "sair":
        break

    print("Selecione o seu status: \n01: Sucesso \n02: Falha")
    status = input("Sua opção: ")
    if status == "01":
        status_escolhido = "sucesso"
    elif status == "02":
        status_escolhido = "falha"
    else:
        print("Digite uma opção válida!")
        continue

    try:
        duracao = int(input("Digite a duração em minutos: "))
    except ValueError:
        print("Duração inválida!")
        continue

    acesso_lista = (usuario, status_escolhido, duracao)
    registros.append(acesso_lista)

    if status_escolhido == "sucesso":
        usuarios_sucesso.add(usuario)
        tempo += duracao
        print("Registro adicionado!")

print(f"Registros de acessos: {registros}")
print(f"Usuários com sucesso no acesso: {usuarios_sucesso}")
print(f"Tempo total das sessões bem sucessidas: {tempo} minutos")
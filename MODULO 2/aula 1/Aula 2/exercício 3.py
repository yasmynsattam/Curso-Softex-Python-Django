#TUPLAS, LOGIN COM SUCESSO E FALHAS
acessos = [("Pedro", "sucesso"), ("Ana", "falha"), ("Maria", "sucesso"), ("Pedro", "falha"), ("Ana", "falha")]

usuarios_sucesso = set()
usuarios_falha = set()

for nome, acesso in acessos:
    if acesso == "sucesso":
        usuarios_sucesso.add(nome)
else:
    usuarios_falha.add(nome)   


print(f'Usuários que tiveram login com falhas:')
print(usuarios_falha.difference(usuarios_sucesso))

print(f'Usuários que tiveram login com sucesso:')
print(usuarios_sucesso)
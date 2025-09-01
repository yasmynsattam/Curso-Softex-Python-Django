''''
Comercio Padaria
1- O programa tem que rodar em loop infinito até ser parado 
2- cliente pedir um tipo de pão (frances, doce, forma, australiano) X
3- cada pao terá uma quantidade X
4- valor do pao X
5- pedir forma de pagamento (dinheiro, cartao)
6- forma de entrega 
7- dados do cliente (se for entregar)
8- valor do frete do bairro X
9- nome do atendente X
10- codigo da entrega
''' 
#Nomes dos paes
pao_frances = "frances"
pao_doce = "doce"
pao_forma = "forma"

#Valor dos paes
valor_frances = 0.50
valor_doce = 5.00
valor_forma = 5.99

#Quantidade dos paes
quantidade_frances = 15
quantidade_doce = 20
quantidade_forma = 18 

#Fundionário
nome_atendente = "maria"

#Nome dos bairros
bairro_barroco = "barroco"
bairro_sao_jose = "sao Jose"

#Valores dos fretes
frete_barroco = 5.00
frete_sao_jose = 15.00

#Código de venda
codigo_venda = 98568

while True: 
    print(f"-- Bem vindo a padaria, Desespero, sou a atendente {nome_atendente} --")
    escolha = input(f'Temos os pães: {pao_frances, pao_doce, pao_forma}. Qual pão deseja?')
    if escolha == pao_frances:
          quantidade = int(input("Qual a quantidade?"))
          if quantidade <= quantidade_frances:
            quantidade_frances -= quantidade
            pedido_de_paes = quantidade
            valor_compra = quantidade * valor_frances
            print(f'Seu pedido ficou em R$ {quantidade* valor_frances}.')
    else:
            print(f'Infelizmente só tenho {quantidade_frances} pães no momento.')
            break
        
    forma_retirada = input("É para 1: retirar ou 2: entregar?").lower()
    if forma_retirada == "2":
            bairro_entrega = input(f'Qual o bairro? (1:{bairro_barroco, 2, bairro_sao_jose}')
            if bairro_entrega == "1":
                valor_frete = frete_barroco
                print(f'Valor do frete R${frete_barroco}')
            elif bairro_entrega == "2":
                valor_frete = frete_sao_jose
                print(f'Valor do frete R${frete_sao_jose}')
            else:
                print("Fora da área de entrega")
                break
    elif forma_retirada == "1":
         valor_frete = 0.00
    else:
         break
    
    dados_cliente = input("Informe seu nome:")
    forma_pagamento = input("Escolha a forma de pagamento (1-dinheiro, 2-cartão):")
    if forma_pagamento == "1":
         forma_pagamento = "Dinheiro"
    else: 
         forma_pagamento = "Cartão"

    codigo_atual = codigo_venda +1
    
    print(f'O valor total da sua compra foi de R$ {valor_compra + valor_frete}')
    break
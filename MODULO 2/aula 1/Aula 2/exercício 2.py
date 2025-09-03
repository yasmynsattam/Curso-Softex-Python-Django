#TUPLAS E CONJUNTOS

estoque_principal = [("camiseta", 100), ("calça", 102), ("boné", 103), ("tênis", 104)]
estoque_online = [("boné", 103), ("camisa polo", 105), ("calça", 102), ("chinelo", 106)]

produtos_loja_fisica = set(estoque_principal)
produtos_loja_online = set(estoque_online)

set_principal = set(estoque_principal)
set_online = set(estoque_online)

em_ambos = set_principal.intersection(set_online)
print("Produtos disponíveis na loja e no site:")
print(em_ambos)

apenas_loja = set_principal.difference(set_online)
print("Produtos disponíveis apenas na loja física:")
print(apenas_loja)

apenas_online = set_online.difference(set_principal)
print("Produtos disponíveis apenas no site:")
print(apenas_online)



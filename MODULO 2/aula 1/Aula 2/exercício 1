#UTILIZANDO TUPLAS, LISTAS E CONJUNTOS

vendas_filtradas = []
produtos_unicos = set()
loja = [("Teclado", 50, 2), ("Mouse", 25.50, 4), ("Monitor", 300, 1), ("Fone", 45, 1), ("Webcam", 75.20, 2)]

for produto, valor, quantidade in loja:
    total_venda = valor * quantidade
    if total_venda >= 100:
        vendas_filtradas.append((produto, valor, quantidade))  

    produtos_unicos.add(produto)
print(produtos_unicos)

print("vendas_filtradas (valor total >= 100):", vendas_filtradas)
print("produtos_unicos (sem duplicatas):", produtos_unicos) 
print("Total de produtos únicos:", len(produtos_unicos))
print("Total de vendas filtradas:", len(vendas_filtradas))


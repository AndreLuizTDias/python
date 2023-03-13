dicionario = {}
print("dicionario vazio", dicionario)

preco_produtos = {"pera": 10,
                 "uva": 15,
                 "maça": 20}

print(preco_produtos)
print(preco_produtos["pera"])
print(preco_produtos["maça"])

print("usando o get", preco_produtos.get("pera"))

preco_produtos["pera"] = 5
print(preco_produtos["pera"])

print(preco_produtos)
del preco_produtos["maça"]
print(preco_produtos)

preco_produtos.clear()
print("limpou o discionario", preco_produtos)

print("="*30)
print("usando for")
print("="*30)

preco_produtos = {"pera": 10,
                 "uva": 15,
                 "maça": 20}

for i, j in preco_produtos.items():
    print(i, j, sep="-")

#imprime somente as chaves
for prod in preco_produtos.keys():
    print(prod)


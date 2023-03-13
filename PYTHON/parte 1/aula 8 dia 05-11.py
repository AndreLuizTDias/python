tupla1 = (1, 2, 3, 4, 5)

print(tupla1)
print("imprimi o 2º indice da tupla", tupla1[1])
print("imprimi o 3º indice da tupla", tupla1[2])

cont = 0

for i in tupla1:
    print(cont, i, sep=("->"))
    cont += 1

print("tem o numero 9 na tupla? ", 9 in tupla1)
print("nao tem o numero 9 na tupla? ", 9 not in tupla1)
print("existe o numero 9 e 8 na tupla? ", 9 and 8 in tupla1)
print("existe o numero 1 e 7 na tupla? ", 1 and 7 in tupla1)
print("existe o numero 1 ou 7 na tupla?", (1 or 7) in tupla1)

print("===================================")
print("verificando o tipo de variavel")
print("===================================")

tupla2 = (5, 6, 7, 8, 9)

lista1 = [1, 2, 3, 4]

print(type(tupla2))
print(type(lista1))
print(type("ola mundo"))
print(type(125))
print(type(3.5))

valor = True
print(type(valor))

print("===================================")
print("convertendo os tipos do valores")
print("="*30)

n1 = 3.14

print(int(n1))
print(3.9989, int(3.9989))

n2 = "280"

print("2345", int("2345"))
print(int(n2))

n3 = int(n2)
print(type(n3))


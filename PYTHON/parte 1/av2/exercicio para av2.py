#1
lista1 = [1,2,3]
lista2 = [4,5,6]
print(lista1 + lista2)
#2
print("{:>10}" .format("teste"))

#5
inventario = {'banana': 50, 'laranja': 12, 'melancia': 7, 'kiwi': 23}

total = 0
for valor in inventario.values():
    total += valor
    print(total)
    print(valor)

print(total)
#6
lista1 = [4, 3, 2, 1]

#lista1.pop()
lista1.remove()

print(lista1)

#7
lista1 = []
size = int(input("informe a quantidade de elementos da lista: "))

while size <= 0:
    if size <= 0:
        print("a quantidade de elementos da lista so pode ser definidos por numeros inteiros acima de 0\n", "porfavor insira outro numero:")
        size = int(input("informe a quantidade de elementos da lista: "))

for i in range(size):
    num = float(input("informe um elemento: "))
    if num % 2 == 0:
        lista1.append(num)

print(lista1)


print("fatiamento da lista")
a = int(input("informe o primeiro indice: "))
b = int(input("informe o ultimo indice: "))

print(lista1[a:b])

#11
import math
def fatorialista():
    for i in range(4):
        print("fatorial:", math.factorial(lista1[i]))

lista1 = []

for i in range(4):
    num = int(input("informe um elemento: "))
    lista1.append(num)

print("elementos da lista: ", lista1)

fatorialista()

#12
class transporte(object):
    def __init__(self, tipo, modelo):
        self.tipo = tipo
        self.modelo = modelo

class terrestre(transporte):
    def __init__(self, tipo, modelo):
        super().__init__(tipo, modelo)

class aquatico(transporte):
    def __init__(self, tipo, modelo):
        super().__init__(tipo, modelo)

terrestre1 = terrestre("carro", "gol")
terrestre2 = terrestre("carro", "uno")

print(terrestre1.tipo, terrestre1.modelo)
print(terrestre2.tipo, terrestre2.modelo)

aquatico1 = aquatico("submarino", "S-BR")
aquatico2 = aquatico("barco", "levefort apolus")

print(aquatico1.tipo, aquatico1.modelo)
print(aquatico2.tipo, aquatico2.modelo)

lista1 = []
size = int(input("informe o numero de elementos da lista:  "))

for i in range(size):
    n = int(input("insira um nº: "))
    lista1.append(n)

num = int(input("informe o numero que sera removido: "))

for i in lista1:
    if num == i:
        lista1.remove(num)

print(lista1)
#----------------------------------

lista1 = [8, 9, 5, 4]
lista2 = [1, 3]

lista3 = lista1 + lista2
lista3.sort()

print(lista3)

#-----------------------------------#

def nomes():
    lista1 = []
    size = int(input("informe a quantidade de nomes que sera inserido: "))

    for i in range(size):
        nome = input("insira um nome: ")
        lista1.append(nome)

    lista1.sort()

    print(lista1)


print("inicio do programa")

nomes()

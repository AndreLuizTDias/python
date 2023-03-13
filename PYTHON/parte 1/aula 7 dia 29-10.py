lista1 = [1, 2, 3, 4]
lista2 = [5, 6, 7, 8]

for i in lista1:
    print(lista1[i-1])

print("==========================================")

print(lista1 + lista2)

print("==========================================")

print("tem o numero 10 na lista 1 ? ", 10 in lista1)
print("tem o numero 5 na lista 2 ? ", 5 in lista2)

print("==========================================")

print("maior elemento da lista 1: ", max(lista1))
print("menor elemento da lista 1: ", min(lista1))

print("==========================================")

print("soma de todos os elementos da lista 1:", sum(lista1))

print("==========================================")

print("quantidade de elementos da lista 1: ", len(lista1))

print("==========================================")
print("==========================================")

lista3 = [5, 6, 7, 8]

lista3.append(9)

print("inseri o num 9 a lista", lista3)

lista3.insert(1, 38)

print("inseri o numero 38 no indice 1", lista3)

lista3.remove(5)

print("removi o numero 5 da lista", lista3)

lista3.pop(1) #remove o elemento do indice 1
lista3.pop() #remove o ultimo elemento da lista

print("removi o elemento no indice 1 e removi o ultimo elemento", lista3)

lista3.clear()

print("limpei a lista 3",lista3)

lista3 = [9, 8, 7, 6]

print("lista 3 com novo valores", lista3)

lista3.sort()

print("ordenei a lista3", lista3)


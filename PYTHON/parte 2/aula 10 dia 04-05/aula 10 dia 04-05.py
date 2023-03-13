#LISTA DE EXERCICIO 10 LISTAS TUPLAS E SET
print("-"*5, "1", "-"*5)
lista1 =[]
i = 0

while i < 3:
    n = int(input("informe um numero "))
    lista1.append(n)
    i += 1

print("maior numero da lista= ", max(lista1))

print("-"*5, "2", "-"*5)

a = set(lista1)
lista2 = [a]
print("lista sem numeros repitidos= ", lista2)

print("-"*5, "3", "-"*5)

exe_tupla = ("orange", [10, 20, 30], (5, 15, 25))
print(exe_tupla)
print(exe_tupla[1][1])

print("-"*5, "4", "-"*5)

lista3 = [23,56,8,7,4,23]
lista3 = set(lista3)
print(lista3)
n1= int(input("informe um numero a ser removido"))

lista3.discard(n1)

print(lista3)
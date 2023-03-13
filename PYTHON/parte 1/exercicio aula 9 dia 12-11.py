#1
def numpares():
    conj = set()
    num1 = 0
    for i in range(0, 5):
        num1 = int(input("insira um numero: "))
        if num1 % 2 == 0:
            conj.add(num1)

    print(conj)

numpares()


#2
a1 = set()
lista1 = []

n = 1
num = 0
while n != 0:
    print("digite um numero")
    num = int(input())
    n = int(input("digite 0 para encerrar o programa"))

    if num % 2 == 0:
        a1.add(num)
    else:
        lista1 = [num]

print(a1)

print(lista1)

#3
lista1 = [1, 2, 3]
lista2 = ["a", "b", "c"]
lista3 = [7, 8, 9]
lista4 = []

for i in range(0, 3):
    lista4.append(lista1[i])
    lista4.append(lista2[i])
    lista4.append(lista3[i])

print(lista4)

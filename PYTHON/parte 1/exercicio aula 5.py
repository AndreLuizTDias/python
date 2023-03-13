print("exercicio 1")
n = 1
qtdpares = 0
qtdimpares = 0
num = 0
while n <= 10:
    print("digitine o ", n,"º numero: ", sep="")
    num = int(input())
    if num % 2 == 0:
        qtdpares += 1
    else:
        qtdimpares += 1
    n += 1

print("quantidades de numeros pares informados= ", qtdpares)
print("quantidades de numeros impares informados= ", qtdimpares)

print("exercicio 2")
n = 1
soma = 0
media = 0
num = 0
while n <= 5:
    print("digite o", n, "º numero: ", sep="")
    num = int(input())
    soma += num
    n += 1
media = soma/5
print("soma=", soma, "e media=", media)

print("exercicio 3")

n = 1
qtde = 0
soma = 0
media = 0
num = 0
while n != 0:
    num = int(input("informe um numero:\n"))
    soma += num
    qtde += 1
    n = int(input("digite 0 caso queira encerrar o programa para continuar digite 1"))
media = soma/qtde
print("foram informados", qtde, "numeros e a media", media)

print("exercicio 4")

multi3 = 0
multi5 = 0
multi4 = 0

for i in range (1,101):
    if (i % 3 == 0):
        print(i,"e multiplo de 3", sep="->")
        multi3 += 1
    if (i % 5 == 0):
        print(i,"e multiplo de 5", sep="->")
        multi5 += 1
    if (i % 4 == 0):
        print(i,"e multiplo de 4", sep="->")
        multi4 += 1

print("quantidade de multiplos de 4: ", multi4)
print("quantidade de multiplos de 3: ", multi3)
print("quantidade de multiplos de 5: ", multi5)

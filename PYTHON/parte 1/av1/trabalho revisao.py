
num1 =int(input('primeiro numero: '))
num2 =int(input('segundo numero: '))

print('soma dos numeros:', num1+num2)
print('subtraçao dos numeros:', num1-num2)
print('multiplicaçao dos numeros:', num1*num2)
print('resto da divisao dos numeros:', num1%num2)

#----------------------------------------
n = 's'
qtde = 0
soma = 0
media = 0
nota = 0
while n == 's' or n == 'S':
    nota = float(input("informe uma nota: "))
    if nota >= 0 and nota <=10:
        soma += nota
        qtde += 1
        n = input("se deseja continuar digite s, caso queria parar aperte qualquer outra tecla")
        media = soma/qtde
    else:
        print("numero invalido")

if media >= 7:
        print("foram informados", qtde, "notas e a media=", media, "aluno aprovado")
elif media <= 5:
        print("foram informados", qtde, "notas e a media=", media, "aluno reprovado")
else:
        print("foram informados", qtde, "notas e a media=", media, "aluno recuperaçao")

#------------------------------------
import math

n1 = int(input("insira um numero: "))
c = n1
f = 1
while c > 0:
    f *= c
    c -= 1
print("fatorial de ",n1,": ",f)

n1 = int(input("insira um numero: "))
print("o fatorial de ", n1, ": ", math.factorial(n1))

#---------------
n = 's'
qtde = 0
soma = 0
media = 0
num = 0
while n == 's' or n == 'S':
    num = int(input("informe o valor de um produto: "))
    soma += num
    qtde += 1
    n = input("se deseja continuar digite s, caso queria parar aperte qualquer outra tecla")

desc = float(input("insira quantos % de desconto: "))
desc = soma*desc/100
desc1 = soma-desc

print("foram informados", qtde, "produtos, valor total=", soma, " valor do desconto= ", desc, "valor total com desconto", desc1)
#-----------------

multi4 = 0

for i in range (1,101):
    if (i % 4 == 0):
        print(i,"e multiplo de 4", sep="->")
        multi4 += 1

multi4 = 0
qtde = 0
for i in range (1,101):
    if (i % 4 == 0):
        print(i,"e multiplo de 4", end=' | ')
        multi4 += 1
        qtde += 1

print("quantidade de multiplos de 4= ", qtde)
#---------------
n1 = int(input("insira o 1º numero"))
n2 = int(input("insira o 2º numero"))
n3 = int(input("insira o 3º numero"))
n4 = int(input("insira o 4º numero"))
n5 = int(input("insira o 5º numero"))

if n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5:
    print("o maior numero informado foi", n1)
if n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5:
    print("o maior numero informado foi", n2)
if n3 > n1 and n3 > n2 and n3 > n4 and n3 > n5:
    print("o maior numero informado foi", n3)
if n4 > n1 and n4 > n2 and n4 > n3 and n4 > n5:
    print("o maior numero informado foi", n4)
if n5 > n1 and n5 > n2 and n5 > n3 and n5 > n4:
    print("o maior numero informado foi", n5)
#--------------

qtde = 1
maior = -9999
while qtde <= 5:
    print("digite o {:d}º numero".format(qtde))
    num = int(input())
    qtde += 1
    if num > maior:
        maior = num
print(maior)
#------------------------
cont = 0
for i in range (1,100):
    if i % 4 == 0:
        print(i, end="|")
        cont +=1
print("\n total:", cont)

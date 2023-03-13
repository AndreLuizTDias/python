print("exercicio 1")

n1 = int(input("insira o primeiro numero: "))
n2 = int(input("insira o segundo  numero: "))

if n1 > 0 and n2 > 0:
    print("sequencia entres os numeros")
    while n1+1 < n2:
        n1 = n1+1
        print("nº:", n1)
else:
    print("somente numeros positivos")

print("exercicio 2")

n1 = int(input("insira um numero: "))
c = n1
f = 1
while c > 0:
    f *= c
    c -= 1
print("fatorial de ",n1,": ",f)

print ("exercicio 3")

cont = 1
n1 = 1
c = 2
for i in range(1, 50):
    n1 += c
    c += 1
    print(n1, end=" ")

#while cont < 50:
#     n1 += c
#     c += 1
#     cont += 1
#     print(n1, end=" ")


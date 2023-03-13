import math
print("exercício 1")

for i in range(1, 11):
    print("o fatorial de ", i, ": ", math.factorial(i))

print("exercício 2")
n = int(input("insira o numero de n: "))
k = int(input("insira o numero de k: "))

if n > k:
    print("numero de combinaçoes do numero", n,"com o numero", k, "e igual a", math.comb(n, k))
else:
    print("sequecia invalida")

print("exercício 3")

print("numero de permutaçoes do numero", n,"com o numero", k, "e igual a", math.perm(n, k))

print("exercício 4")

co = float(input("insira o valor do cateto oposto: "))
ca = float(input("insira o valor do cateto adjacente: "))

res = math.hypot(co, ca)

print("a hipotenusa dos catetos informados e =", round(res, 2))

print("exercício 5")

x = float(input("insira o valor de x: "))
b = float(input("insira o valor da base: "))

if b > 0:
    print("o logaritmo de", x, "na base", b, "= ", math.log(x, b))
else:
    print("o logaritmo natural de", x, "= ", math.log(x, 2.71))

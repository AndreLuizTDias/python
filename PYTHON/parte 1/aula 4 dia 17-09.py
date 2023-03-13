#x = 2 int(input("insira o valor de x:"))
#y = 2 int(input("insira o valor de y:"))

#print(x, "elevado a", y, "=", pow(x, y))

#exercicio
l=0
for i in range(0,11):
    print(2, "elevado a", l, "=", pow(2,l))
    l += 1

l=0
for i in range(0,11):
    print(3, "elevado a", l, "=", pow(3,l))
    l += 1

#exercicio 2
nota1 = float(input("insira a 1ºnota: "))
nota2 = float(input("insira a 2ºnota: "))
nota3 = float(input("insira a 3ºnota: "))

media = (nota1+nota2+nota3)/3
print("media =", round(media,2))

#exercicio 3
num = int(input("insira um numero: "))
c= 1
for i in range(0, 10):
    print(num, "+",c ,"=", num+c)
    c += 1
c= 1
for i in range(0, 10):
    print(num, "x" ,c ,"=", num*c)
    c += 1

print("exemplo 1")
nota = float(input("inseira a nota:"))
if nota >=7:
    print("aprovado")
elif nota <=5:
    print("reprovado")
else:
    print("recuperaçao")

print("---------------------------")
print("exemplo 2")

idade = int(input("insira a idade: "))

if idade <=12:
    print("criança")
elif idade <=17:
    print("adolescente")
elif idade <=59:
    print("adulto")
else:
    print("idoso")

print("---------------------------")

a= int(input("insira um numero: "))
b= int(input("insira outro numero: "))

if (a>10 and b >10):
    print("numeros maiores que 10")
else:
    print("um dois numeros e menor que 10")

print("---------------------------")

a= int(input("insira um numero: "))
b= int(input("insira outro numero: "))

if (a>10 or b >10):
    print("numeros maiores que 10")
else:
    print("um dois numeros e menor que 10")

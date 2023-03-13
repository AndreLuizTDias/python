def Imprimir_tela():
    print("testando esse print")

Imprimir_tela()

def Soma_valores(a, b):
    print("soma =", a+b)

print("inicio do programa")
a=int(input("informe o 1ºnumero"))
b=int(input("informe o 1ºnumero"))

Soma_valores(a, b)

def Calcula_fatorial(numero):
    fatorial = 1
    while numero >0:
        fatorial = fatorial * numero
        numero -= 1
    return fatorial

numero = int(input("digite o numero: "))
fat = Calcula_fatorial(numero)
print("fatorical c/ repetiçao:", fat)



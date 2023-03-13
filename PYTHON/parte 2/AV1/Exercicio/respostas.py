#6
lista1 = []
opc = 1

while opc == 1:
    num = int(input("insira um numero "))
    lista1.append(num)
    opc = int(input("digite 1 para continuar | 0 para sair"))

print("numeros inseridos ", lista1)
print("maior numero inserido= ", max(lista1))
#7
import string
conjunto = input("insira o conjunto ")

alfabeto = list(string.ascii_letters)
num = list(string.digits)
simb = list(string.punctuation)

letras = 0
numeros = 0
simbulos = 0

for i in conjunto:
    if i in alfabeto:
        letras += 1
    if i in num:
        numeros += 1
    if i in simb:
        simbulos += 1

print("a string", conjunto, "possue", letras, "letras ", numeros, "numeros e ", simbulos, "simbulos")
#8
p1 = input("insira uma palavra ")
p2 = input("insira outra palavra ")

p3 = (p2[:2]+p1[2:]+" "+p1[:2]+p2[2:])

print(p3)
#9
n1 = 0
n2 = 1
n3 = 0
opc = 0
print("a sequencia Fibonacci")
print(n1, "-", n2, end=" - ")

while opc < 8:
    n3 = n1+n2
    print(n3, end=" - ")
    n1 = n2
    n2 = n3
    opc += 1

#10
import sqlite3

connection = sqlite3.connect("bebidas.db")
tabela = connection.cursor();
# Criando tabela
tabela.execute("""CREATE TABLE bebidas
                  (codigo INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                  marca_bebida TEXT NOT NULL, 
                  tipo_bebida TEXT, 
                  data_validade DATE,
                  indicacao BOOLEAN,
                  preco REAL);""")
connection.commit()
#inserindo dados
print("-"*30)
marca_bebida = input("marca da bebida: ")
tipo_bebida= input("tipo da bebida: ")
data_validade = input("data de validade em (aaa,MMM,ddd): ")
indicacao = input("A bebida e alcoolica ? digite true para sim | false para nao: ")
preco = input("preço= ")

tabela.execute("""INSERT INTO bebidas(marca_bebida, tipo_bebida, data_validade, indicacao, preco) VALUES (?,?,?,?,?)""",
               (marca_bebida, tipo_bebida, data_validade, indicacao, preco))

connection.commit()
#mostra os dados
for i in tabela.execute("SELECT * FROM bebidas"):
    print(i)

# Atualiza o preço de uma bebida insirada na tabela
novo_preco = input("informe novo preço")
codigo_bebida = input("insira o codigo da bebida")

tabela.execute("""UPDATE bebidas SET preco = ? WHERE codigo = ?""", (novo_preco, codigo_bebida))
connection.commit()
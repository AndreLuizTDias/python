import sqlite3

connection = sqlite3.connect("bebidas.db")
tabela = connection.cursor();

for i in tabela.execute("SELECT * FROM bebidas"):
    print(i)
connection.commit()
# Atualiza o preço de uma bebida insirada na tabela
novo_preco = input("informe novo preço")
codigo_bebida = input("insira o codigo da bebida")

tabela.execute("""UPDATE bebidas SET preco = ? WHERE codigo = ?""", (novo_preco, codigo_bebida))
connection.commit()

for i in tabela.execute("SELECT * FROM bebidas"):
    print(i)
connection.commit()

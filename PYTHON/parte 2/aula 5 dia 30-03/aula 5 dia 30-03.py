import sqlite3

connection = sqlite3.connect("mydatabase.db")
tabela = connection.cursor();

#tabela.execute("""CREATE TABLE dados
#                  (nome, rg, cpf, data_nasc)""")


#tabela.execute("INSERT INTO dados VALUES"
#               "('Maria', '00235','23456789','14/02/1980')")

tabela.execute("""SELECT * FROM dados""")
connection.commit()


import sqlite3
connection = sqlite3.connect("BD1.db")

tabela = connection.cursor();


nome = input("informe o nome do livro ")
pesq = "SELECT codigo_livro, nome_livro, volume, num_paginas, preco FROM livraria WHERE nome_livro = ?"

tabela = connection.execute(pesq, [(nome)])
resp = tabela.fetchall()

connection.commit()


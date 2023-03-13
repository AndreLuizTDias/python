def coletar_dados(linha):
    nome = linha[0]
    idade = linha[1]
    cidade = linha[2]
    nota1 = linha[3]
    nota2 = linha[4]
    media = (float(nota1)+float(nota2))/2
    print(nome,idade,cidade,nota1,nota2,media)
    tabela.execute("""INSERT INTO BD1 (nome, idade, cidade, nota1, nota2, media) VALUES (?,?,?,?,?,?)""", (nome, idade, cidade, nota1, nota2, media))

import sqlite3

connection = sqlite3.connect("BD1.db")
tabela = connection.cursor();

tabela.execute("""CREATE TABLE dados
                  (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                  nome TEXT NOT NULL, 
                  idade INTERGER, 
                  cidade TEXT,
                  nota1 REAL
                  nota2 REAL
                  media REAL);""")
connection.commit()


arquivo = open("infos.txt", "r", encoding="utf-8")
for i in arquivo:
    coletar_dados(i.split())
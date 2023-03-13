def coletar_dados(linha):
    nome = linha[0]
    idade = linha[1]
    cidade = linha[2]
    nota1 = linha[3]
    nota2 = linha[4]
    media = (float(nota1)+float(nota2))/2
    print(nome, idade, cidade, nota1, nota2, media)
    tabela.execute("""INSERT INTO dados (nome, idade, cidade, nota1, nota2, media) VALUES (?,?,?,?,?,?)""", (nome, idade, cidade, nota1, nota2, media))
    connection.commit()

import sqlite3

connection = sqlite3.connect("BD1.db")
tabela = connection.cursor();


arquivo = open("infos.txt", "r", encoding="utf-8")
for i in arquivo:
    coletar_dados(i.split())
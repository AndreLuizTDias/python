import sqlite3
connection = sqlite3.connect("repostaexer6.db")
tabela = connection.cursor();

def coletar_dados(linha):
    nome = linha[0]
    idade = linha[1]
    cidade = linha[2]
    nota1 = linha[3]
    nota2 = linha[4]
    media = (float(nota1)+float(nota2))/2
    print(nome, idade, cidade, nota1, nota2, media)
    tabela.execute("""INSERT INTO alunos (nome, idade, cidade, nota1, nota2, media) VALUES (?,?,?,?,?,?)""", (nome, idade, cidade, nota1, nota2, media))
    connection.commit()

#tabela.execute("""
#    CREATE TABLE alunos(
#            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#            nome TEXT NOT NULL,
#            idade INTEGER,
#            cidade TEXT,
#            nota1 REAL,
#            nota2 REAL,
#            media REAL);
#               """)
#print('tabela -- alunos -- criada com sucesso no bd.')
#connection.commit()

arquivo = open("infos.txt", "r", encoding="utf-8")
for i in arquivo:
    coletar_dados(i.split())


tabela = connection.execute("SELECT id, nome, idade, cidade, nota1, nota2, media from alunos")
template = "{0:<5}|{1:10}|{2:<10}|{3:10}|{4:<7}|{5:<7}|{6:<7}"
print(template.format("ID", "NOME", "IDADE", "CIDADE", "NOTA 1", "NOTA 2", "MEDIA FINAL"))
for i in tabela:
    print(template.format(*i))

connection.commit()

sql_search=("SELECT * FROM alunos where ID ?")

tabela.execute("SELECT nome FROM alunos")
a=tabela.fetchall()

print(a)
print(type(a))

import psycopg2
conn = psycopg2.connect(database="postgres", user="postgres", password="1", host="127.0.0.1", port="5432")

print("Conexao com o banco de dados aberta com sucesso!")

cur = conn.cursor()
cur.execute('''CREATE TABLE Agenda
(ID INT PRIMARY KEY NOT NULL, 
Nome TEXT NOT NULL, 
Telefone CHAR(12));''')
conn.commit()
print("Tabela criada com sucesso!")

#inserçao de dados
cur = conn.cursor()
cur.execute('''INSERT INTO public."agenda"("id","nome","telefone") VALUES (1,'pessoa 1','02199999999')''')

print("inserçao realizada com sucesso!")

conn.commit()
# SELEÇAO DOS DADOS
cur = conn.cursor()
cur.execute('''SELECT * FROM public."agenda" WHERE "id"=1''')
registro = cur.fetchone()
print(registro)

conn.commit()
print("seleçao realizada com sucesso!")

#Mostra os dados sem atualizaçao
cur = conn.cursor()
cur.execute('''SELECT * FROM public."agenda" WHERE "id"=1''')
registro = cur.fetchone()
print(registro)

#atualizaçao de um unico registro
cur.execute('''Update public."agenda" set "telefone"=0123456789 WHERE "id"=1''')
conn.commit()
print("Registro atualizado com sucesso!")

#pesquisa depois da atualizaçao
cur = conn.cursor()
print("Consulta apos a atualizaçao")
cur.execute('''SELECT * FROM public."agenda" WHERE "id"=1''')
registro = cur.fetchone()
print(registro)
conn.commit()

#EXCLUSAO DE DADOS
cur = conn.cursor()
cur.execute('''DELETE FROM public."agenda" WHERE "id"=1''')
conn.commit()
cont = cur.rowcount #A propriedade “rowcount” do “cursor” retorna a quantidade de registros que foram excluídos da tabela “Agenda”.
print(cont, "Registro excluido com sucesso")
print("Exclusao realizada com sucesso")

conn.close()
import psycopg2

class AppBD:
    def __init__(self):
        print("metodo construtor")

    def abrirConexao(self):
        try:
            self.connection = psycopg2.connect(user="postgres",
                                               password="1",
                                               host="127.0.0.1",
                                               port="5432",
                                               database="postgres")
        except(Exception, psycopg2.Error) as error:
            if(self.connection):
                print("Falha ao se conectar ao banco de dados", error)

    def selecionarDados(self):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()

            print("Selecionando todos os produtos")
            sql_select_querry = """select * from public."PRODUTO" """

            cursor.execute(sql_select_querry)
            registros= cursor.fetchall()
            print(registros)

        except (Exception, psycopg2.Error) as error:
            print("Error in select operation", error)

        finally:
            if(self.connection):
                cursor.close()
                self.connection.close()
                print("A conexao com o postgresSQL foi fechada.")
        return registros

    def inserirDados(self, codigo, nome, preco):
        try:
            self.abrirConexao()

            cursor = self.connection.cursor()
            postgres_insert_querry = """INSERT INTO public."PRODUTO"
            ("codigo","nome","preco") VALUES (%s,%s,%s)"""
            record_to_insert = (codigo, nome, preco)
            cursor.execute(postgres_insert_querry, record_to_insert)
            self.connection.commit()

            count = cursor.rowcount
            print(count, "Registro inserido com sucesso na tabela produto")
        except (Exception, psycopg2.Error) as error:
            if(self.connection):
                print("falha ao inserir registro na tabela produto", error)
        finally:
            if(self.connection):
                cursor.close()
                self.connection.close()
                print("A conexao com o PostgreSQL foi fechado.")

    def atualizarDados(self, codigo, nome,preco):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()

            print("Registro Antes da atualizaçao")
            sql_select_querry = """select * from public."PRODUTO" 
            where "codigo" = %s """
            cursor.execute(sql_select_querry, (codigo,))
            record = cursor.fetchone()
            print(record)
            #atualizar registro
            sql_update_query = """UPDATE public."PRODUTO" 
            set "nome"= %s,"preco"= %s where "codigo"= %s """
            cursor.execute(sql_update_query, (nome, preco, codigo))
            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro atualizado com sucesso")
            print("Depois da atualizaçao")
            sql_select_querry = """select * from public."PRODUTO" 
            where "codigo" = %s """
            cursor.execute(sql_select_querry, (codigo,))
            record = cursor.fetchone()
            print(record)

        except (Exception, psycopg2.Error) as error:
            print("Erro na atualizaçao", error)
        finally:
            if(self.connection):
                cursor.close()
                self.connection.close()
                print("A conexao com o postgres foi fechada.")

    def excluirDados(self, codigo):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            #atualizando registro
            sql_delete_query = """Delete from public."PRODUTO" 
            where "codigo"= %s """
            cursor.execute(sql_delete_query, (codigo))

            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro excluido com sucesso")
        except(Exception, psycopg2.Error) as error:
            print("Erro na Exclusao", error)
        finally:

            if(self.connection):
                cursor.close()
                self.connection.close()
                print("Conexao com o postgres foi fechada.")
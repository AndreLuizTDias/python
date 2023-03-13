import psycopg2
import tkinter as tk
from tkinter import ttk
import crud as crud

conn = psycopg2.connect(database="postgres", user="postgres", password="1", host="127.0.0.1", port="5432")

print("Conexao estabelecida com sucesso")

#CRIAÇAO DA TABELA
cur = conn.cursor()
cur.execute('''CREATE TABLE "PRODUTO"(CODIGO INT PRIMARY KEY NOT NULL,NOME TEXT NOT NULL,PRECO REAL NOT NULL);''')
print("TABELA CRIADA COM SUCESSO")
conn.commit()
conn.close()
# GERAÇAO DE DADOS ALEATORIOS

from faker import Faker
import psycopg2
conn = psycopg2.connect(database="postgres", user="postgres", password="1", host="127.0.0.1", port="5432")
print("Conexao estabelecida com sucesso")

cursor = conn.cursor()
fake = Faker('pt_BR')
n=10
for i in range(n):
    codigo = i+10
    nome='produto_'+str(i+1)
    preco = fake.pyfloat(left_digits=3,right_digits=2,positive=True,min_value=5,max_value=1000)
    print(preco)
    print(nome)

    comandoSQL = """INSERT INTO public."PRODUTO"("codigo","nome", "preco") VALUES (%s,%s,%s)"""
    registro = (codigo, nome, preco)
    cursor.execute(comandoSQL, registro)

conn.commit()
print("INSERÇAO DE DADOS ALEATORIOS REALIZADA COM SUCESSO")

conn.close()

# INTERAÇAO COM O BANCO DE DADOS

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

# INTERFACE GRAFICA
class PrincipalBD:
    def __init__(self, win):
        self.objBD = crud.AppBD()
        #componentes
        self.lblCodigo = tk.Label(win, text='Codigo do Produto: ')
        self.lblNome = tk.Label(win, text='Nome do produto ')
        self.lblPreco = tk.Label(win, text='Preço')

        self.txtCodigo =tk.Entry(bd=3)
        self.txtNome = tk.Entry()
        self.txtPreco = tk.Entry()
        self.btnCadastrar = tk.Button(win, text="Cadastrar", command=self.fCadastrarProduto)
        self.btnAtualizar = tk.Button(win, text="atualizar", command=self.fAtualizarProduto)
        self.btnExcluir = tk.Button(win, text="excluir", command=self.fExcluirProduto)
        self.btnLimpar = tk.Button(win, text="limpar", command=self.fLimparTela)
        #componete ThreeView
        self.dadosColunas = ("Código", "Nome", "Preço")

        self.treeProdutos = ttk.Treeview(win, columns=self.dadosColunas, selectmode='browse')
        self.verscrlbar = ttk.Scrollbar(win, orient="vertical", command=self.treeProdutos.yview)
        self.verscrlbar.pack(side='right', fill='x')

        self.treeProdutos.configure(yscrollcommand=self.verscrlbar.set)

        self.treeProdutos.heading("Código", text="Código")
        self.treeProdutos.heading("Nome", text="Nome")
        self.treeProdutos.heading("Preço", text="Preço")

        self.treeProdutos.column("Código", minwidth=0, width=100)
        self.treeProdutos.column("Nome", minwidth=0, width=100)
        self.treeProdutos.column("Preço", minwidth=0, width=100)

        self.treeProdutos.pack(padx=10, pady=10)

        self.treeProdutos.bind("<<TreeviewSelect>>", self.apresentarRegistrosSelecionados)
        #posicionamento dos componentes na janela
        self.lblCodigo.place(x=100, y=50)
        self.txtCodigo.place(x=250, y=50)

        self.lblNome.place(x=100, y=100)
        self.txtNome.place(x=250, y=100)

        self.lblPreco.place(x=100, y=150)
        self.txtPreco.place(x=250, y=150)

        self.btnCadastrar.place(x=100, y=200)
        self.btnAtualizar.place(x=200, y=200)
        self.btnExcluir.place(x=300, y=200)
        self.btnLimpar.place(x=400, y=200)

        self.treeProdutos.place(x=100, y=300)
        self.verscrlbar.place(x=805, y=300, height=225)
        self.carregarDadosIniciais()

    def apresentarRegistrosSelecionados(self, event):
        self.fLimparTela()
        for selection in self.treeProdutos.selection():
            item = self.treeProdutos.item(selection)
            codigo,nome,preco = item["values"][0:3]
            self.txtCodigo.insert(0, codigo)
            self.txtNome.insert(0, nome)
            self.txtPreco.insert(0, preco)

    def carregarDadosIniciais(self):
        try:
            self.id = 0
            self.iid = 0
            registros =self.objBD.selecionarDados()
            print("***** dados disponiveis no BD *****")
            for item in registros:
                codigo = item[0]
                nome = item[1]
                preco = item[2]
                print("Codigo= ", codigo)
                print("Nome= ", nome)
                print("Preço= ",preco,"\n")

                self.treeProdutos.insert('', 'end',
                                         iid=self.iid,
                                         values=(codigo,
                                                 nome,
                                                 preco))
                self.iid = self.iid + 1
                self.id = self.id + 1
            print("dados de base")
        except:
            print("ainda nao existem dados para carregar")

    # ler dados da tela
    def fLerCampos(self):
        try:
            print("Dados disponiveis")
            codigo = int(self.txtCodigo.get())
            print('codigo', codigo)
            nome = self.txtNome.get()
            print('nome', nome)
            preco = float(self.txtPreco.get())
            print('peco', preco)
            print('Leitura dos dados com sucesso')
        except:
            print("nao foi possivel ler os dadods")
        return codigo, nome, preco

    # cadastrar produto

    def fCadastrarProduto(self):
        try:
            print("dados disponiveis")
            codigo, nome, preco= self.fLerCampos()
            self.objBD.inserirDados(codigo, nome, preco)
            self.treeProdutos.insert('', 'end', iid=self.iid, values= (codigo, nome, preco))
            self.iid = self.iid + 1
            self.id = self.id + 1
            self.fLimparTela()
            print("produto cadastrado com sucesso")
        except:
            print("nao foi possivel fazer o cadastro")

#atualizar produtos
    def fAtualizarProduto(self):
        try:
            print("dados disponiveis")
            codigo, nome, preco = self.fLerCampos()
            self.objBD.atualizarDados(codigo, nome, preco)
            # recarregar daods na tela
            self.treeProdutos.delete(*self.treeProdutos.get_children())
            self.carregarDadosIniciais()
            self.fLimparTela()
            print("produto atualizado com sucesso")
        except:
            print("nao foi possivel fazer a atualizaçao")
# excluir produto

    def fExcluirProduto(self):
        try:
            print("dados disponiveis")
            codigo, nome, preco = self.fLerCampos()
            self.objBD.excluirDados(codigo)
            #recarregar dados da tela
            self.treeProdutos.delete(*self.treeProdutos.get_children())
            self.carregarDadosIniciais()
            self.fLimparTela()
            print("produto excluido com sucesso")
        except:
            print("nao foi possivel fazer a exclusao do produto")
    # limpar tela
    def fLimparTela(self):
        try:
            print("dados disponiveis")
            self.txtCodigo.delete(0, tk.END)
            self.txtNome.delete(0, tk.END)
            self.txtPreco.delete(0, tk.END)
            print("campos limpos")
        except:
            print("nao foi possivel limpar os campos")

janela = tk.Tk()
principal = PrincipalBD(janela)
janela.title("Bem vindo a aplicaçao de banco de dados")
janela.geometry("820x600+10+10")
janela.mainloop()

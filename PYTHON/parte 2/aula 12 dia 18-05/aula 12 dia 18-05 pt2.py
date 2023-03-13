import sqlite3 as lite
from sqlite3 import Error
import tkinter as tk

def criar_BD(bd):
    try:
        connection = lite.connect(bd)
        return connection
    except Error as captura:
        print("Esse BD ja existe!")
        print(captura)


class Win(object):
    def __init__(self):
        self.tela = tk.Tk()
        self.tela.title('usando banco de dados')
        texto = tk.Label(self.tela, text="Insira o nome do BD:")
        texto.pack()
        bd = tk.StringVar()
        nome_bd = tk.Entry(self.tela, textvariable=bd)
        nome_bd.pack()
        botao = tk.Button(self.tela, text="Criar banco de dados", command=criar_BD(bd.get()))
        botao.pack()
        self.tela.mainloop()

win = Win()

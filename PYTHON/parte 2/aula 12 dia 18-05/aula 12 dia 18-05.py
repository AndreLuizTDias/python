import tkinter as tk
from tkinter import ttk
'''
class Application:
    def __init__(self, master=None):
        janela.title("Trabalhando GUI em python")
        botao = tkinter.Button(janela, text="Botao da tela", fg="blue")
        botao.pack()

janela = tkinter.Tk()
Application(janela)
janela.mainloop()
'''
'''
#exemplo 3

class Application:
    def __init__(self, master=None):
        janela.title("Trabalhando GUI EM PYTHON")
        self.tela1 = Frame(master)
        self.tela1.pack()
        self.msg= Label(self.tela1, text="Hello World")
        self.msg.pack()
        self.botao = tkinter.Button(janela, text="Fechar", command=self.tela1.quit)
        self.botao.pack()

janela = tkinter.Tk()
Application(janela)
janela.mainloop()
'''
'''
#exemplo 4

class Application:
    def __init__(self, master=None):
        janela.title("Telas frames")
        self.tela1 = Frame(master)
        self.tela1.pack()
        self.msg = Label(self.tela1, text="Hello World 1")
        self.msg.pack()
        self.botao = tkinter.Button(janela, text="Fechar", command=self.tela1.quit)
        self.botao.pack()
        self.tela2 = Frame(master)
        self.tela2.pack()
        self.msg = Label(self.tela2, text="Hello World 2")
        self.msg.pack()
        self.botao = Button(self.tela2, text="Cancelar", command=self.tela2.quit)
        self.botao.pack()

janela = tkinter.Tk()
Application(janela)
janela.mainloop()

'''
'''
#exemplo 5 usando dicionarios
class Application:
    def __init__(self, master=None):
        janela.title("Trabalhando GUI EM PYTHON")
        self.tela1 = Frame(master)
        self.tela1.pack()
        self.msg= Label(self.tela1)
        self.msg["text"] = "Hello World"
        self.msg.pack()
        self.botao = Button(self.tela1)
        self.botao["text"] = "Fechar"
        self.botao["command"] = self.tela1.quit
        self.botao.pack()

janela = tk.Tk()
Application(janela)
janela.mainloop()
'''
'''
#exemplo 6
def mostrar_nomes():
    print("nome: %s\nsobrenome: %s" % (e1.get(), e2.get()))

janela = tk.Tk()
janela.title("aplicaçao GUI com widget Entry")
tk.Label(janela, text="Nome", fg="blue").grid(row=0)
tk.Label(janela, text="sobrenome").grid(row=1)

e1 = tk.Entry(janela)
e2 = tk.Entry(janela)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

tk.Button(janela, text="sair", command=janela.quit).grid(row=3, column=0, sticky=tk.W, pady=4)
tk.Button(janela, text="Exibir dados", command=mostrar_nomes).grid(row=3,column=1, sticky= tk.W, pady=4)

tk.mainloop()
'''
'''
#exemplo 7
def escolhe_linguag():
    escolha=v.get()
    if escolha == 1:
        print("A linguagem escolhida foi Python!")
    elif escolha == 2:
        print("A linguagem escolhida foi c++!")
    else:
        print("A linguagem escolhida foi Java!")

janela = tk.Tk()
v = tk.IntVar()
tk.Label(janela, text="""Escolha uma linguagem de programação:""", justify=tk.LEFT, padx=20).pack()
tk.Radiobutton(janela, text="Python", padx=25, variable=v, value=1).pack(anchor=tk.W)
tk.Radiobutton(janela, text="C++", padx=25, variable=v, value=2).pack(anchor=tk.W)
tk.Radiobutton(janela, text="C++", padx=25, variable=v, value=3).pack(anchor=tk.W)
tk.Button(janela, text="Imprime escolha", command=escolhe_linguag).pack()
janela.mainloop()

'''

#exemplo 8

janela= tk.Tk()
janela.title("usando Combobox")
janela.geometry('400x250')

ttk.Label(janela, text="exemplo de combobox widget",
          background='green', foreground='white',
          font=("Times New Roman", 15)).grid(row=0, column=1)

ttk.Label(janela, text="Selecione um mês:",
          font=("Times New Roman", 12)).grid(row=5, column=1, padx=10, pady=25)

n = tk.StringVar()
escolha = ttk.Combobox(janela, width=27, textvariable=n)
escolha['values'] = ('Janeiro', 'Fevereiro','Março', 'Abril', 'Maio', 'Junho',
                   'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
escolha.grid(row=5, column=1)
escolha.current()
janela.mainloop()

#exemplo 9 aula 12 pt2
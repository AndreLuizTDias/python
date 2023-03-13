import tkinter
from tkinter import *
'''
janela = tkinter.Tk()
janela.title("trabalhando GUI em python")
botao=tkinter.Button(janela, text="botao da tela")
botao.pack()
janela.resizable(False, True)
janela.mainloop()

janela = tkinter.Tk()
janela.title("Botoes c/ metodos pack()")
botao = tkinter.Button(janela, text="botao da tela").pack(side="left")
janela.mainloop()

janela = tkinter.Tk()
janela.title("Botoes de escolha")
checkVar1 = IntVar()
checkVar2 = IntVar()

tkinter.Checkbutton(janela, text="Machine learning", variable=checkVar1, onvalue=1, offvalue=0).grid(row=0, sticky=W)
tkinter.Checkbutton(janela, text="Deep learning", variable=checkVar1, onvalue=0, offvalue=1).grid(row=1, sticky=W)

janela.mainloop()
'''
#aplicaçoes com classe
class Application:
    def __init__(self, master=None):
        janela.title("Trabalhando GUI em python")
        botao = tkinter.Button(janela, text="Botao da tela", fg="blue")
        botao.pack()

janela = tkinter.Tk()
Application(janela)
janela.mainloop()





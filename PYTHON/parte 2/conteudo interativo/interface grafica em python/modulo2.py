import tkinter as tk

'''
#contador
contador = 0
def contador_label(lblRotulo):
    def funcao_contar():
        global contador
        contador = contador + 1
        lblRotulo.config(text=str(contador))
        lblRotulo.after(1000, funcao_contar)
    funcao_contar()


janela = tk.Tk()
janela.title("Contagem dos Segundos")
lblRotulo = tk.Label(janela, fg="blue")
lblRotulo.pack()
contador_label(lblRotulo)
btnAcao = tk.Button(janela, text='Clique aqui para Interromper a contagem', width=50, command=janela.destroy)
btnAcao.pack()
janela.mainloop()

'''
'''
#ENTRY
def mostrar_nomes():
    print("nome: %s\nsobrenome: %s" % (e1.get(), e2.get()))

janela = tk.Tk()
janela.title("aplicaçao GUI com widget Entry")
tk.Label(janela, text="Nome", fg="blue").grid(row=0)
tk.Label(janela, text="sobrenome").grid(row=1)

e1= tk.Entry(janela)
e2= tk.Entry(janela)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

tk.Button(janela, text="sair", command=janela.quit).grid(row=3, column=0, sticky=tk.W, pady=4)
tk.Button(janela, text="Exibir dados", command=mostrar_nomes).grid(row=3,column=1, sticky= tk.W, pady=4)

tk.mainloop()
'''
'''
Radiobutton
import tkinter as tk
janela = tk.Tk()
v = tk.IntVar()
tk.Label(janela, text="""Escolha uma linguagem de programação:""", justify=tk.LEFT, padx=20).pack()
tk.Radiobutton(janela, text="Python", padx= 5, variable=v, value=1).pack(anchor=tk.W)
tk.Radiobutton(janela, text="C++", padx=25, variable=v, value=2).pack(anchor=tk.W)

janela.mainloop()
'''
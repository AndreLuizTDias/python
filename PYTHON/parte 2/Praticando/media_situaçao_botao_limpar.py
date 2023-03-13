import tkinter as tk
import tkinter as tk

def limpar():
    #limpar campos de entrada ENTRY
    matri.delete(0, "end")
    aluno.delete(0, "end")
    e1.delete(0, "end")
    e2.delete(0, "end")

    # limpar media e situaçao que sao caixa de texto
    Tsitu.delete("1.0", "end")
    Tmedia.delete("1.0", "end")

def mostrar_media():
    n1 = int(e1.get())
    n2 = int(e2.get())
    n3 = (n1 + n2) / 2
    # situaçao
    if n3 >= 6:
        Tsitu.insert(tk.END, "APROVADO")

    elif n3 < 4:
        Tsitu.insert(tk.END, "REPROVADO")
    else:
        Tsitu.insert(tk.END, "RECUPERAÇAO")
    #media
    Tmedia.insert(tk.END, n3)

    tk.mainloop()


# janela principal
janela = tk.Tk()
janela.title("aplicaçao GUI com widget Entry")
janela.geometry("800x450")

tk.Label(janela, text="SISTEMA BASICO").grid(row=0, column=2)
tk.Label(janela, text="matricula").grid(row=2)
tk.Label(janela, text="aluno").grid(row=2, column=2)
tk.Label(janela, text="Nota1").grid(row=4)
tk.Label(janela, text="Nota2").grid(row=4, column=2)
tk.Label(janela, text="media").grid(row=6)
tk.Label(janela, text="situaçao").grid(row=6, column=2)

matri = tk.Entry(janela)
aluno = tk.Entry(janela)
e1 = tk.Entry(janela)
e2 = tk.Entry(janela)


Tmedia = tk.Text(janela, height=1, width=15)
Tsitu = tk.Text(janela, height=1, width=15)

matri.grid(row=2, column=1)
aluno.grid(row=2, column=3)
e1.grid(row=4, column=1)
e2.grid(row=4, column=3)

Tmedia.grid(row=6, column=1)
Tsitu.grid(row=6, column=3)

tk.Button(janela, text="sair", command=janela.quit).grid(row=10, column=0, sticky=tk.W, pady=4)
tk.Button(janela, text="mostrar media", command=mostrar_media).grid(row=10, column=1, sticky=tk.W, pady=4)
tk.Button(janela, text="Limpar", command=limpar).grid(row=10, column=2, sticky=tk.W, pady=4)

tk.mainloop()

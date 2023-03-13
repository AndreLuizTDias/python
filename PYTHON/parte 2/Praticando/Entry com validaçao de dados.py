import tkinter as tk
from tkinter import ttk

def validar_login_senha():
    l=login.get()
    s=senha.get()
    if l == "admin" and s == "123":
        mens=("Login e Senha corretos")

    else:
        mens=("login ou senha invalidos")

    janela = tk.Tk()
    T = tk.Text(janela, height=10, width=100)
    T.pack()
    T.insert(tk.END, mens)
    tk.mainloop()


# janela principal
janela = tk.Tk()
janela.title("aplicaçao GUI com widget Entry, e retorno com Caixa de texto")
janela.geometry("450x450")

tk.Label(janela, text="Login").grid(row=0)
tk.Label(janela, text="Senha").grid(row=1)

login=tk.Entry(janela, justify=tk.RIGHT)
senha=tk.Entry(janela, justify=tk.CENTER, show="*")

senha.grid(row=1, column=1)
login.grid(row=0, column=1)

tk.Button(janela, text="sair", command=janela.quit).grid(row=10, column=0, sticky=tk.W, pady=4)
tk.Button(janela, text="Entrar", command=validar_login_senha).grid(row=10,column=1, sticky=tk.W, pady=4)

tk.mainloop()
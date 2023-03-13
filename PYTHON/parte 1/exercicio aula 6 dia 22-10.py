def Nota():
    n = 's'
    qtde = 0
    soma = 0
    media = 0
    nota = 0
    while n == 's' or n == 'S':
        nota = float(input("informe uma nota: "))
        if (nota >= 0) and (nota <= 10):
            soma += nota
            qtde += 1
            n = input("se deseja continuar digite s, caso queria parar aperte qualquer outra tecla")
            media = soma / qtde
        else:
            print("numero invalido")
    if media >= 7:
        print("foram informados", qtde, "notas e a media=", media, "aluno aprovado")
    elif media <= 5:
        print("foram informados", qtde, "notas e a media=", media, "aluno reprovado")
    else:
        print("foram informados", qtde, "notas e a media=", media, "aluno recuperaçao")


print("inicio do programa")

Nota()


def Media():
    n = 1
    qtde = 0
    soma = 0
    media = 0
    num = 0
    while n != 0:
        num = int(input("informe um numero:\n"))
        soma += num
        qtde += 1
        n = int(input("digite 0 caso queira encerrar o programa para continuar digite 1"))
    media = soma / qtde
    print("foram informados", qtde, "numeros e a media", media)


print("inicio do programa")

Media()


def Idade():
    nome = input("insera seu nome: ")
    idade = int(input('insira sua idade: '))
    ano = (2020 - idade)
    if idade >= 17:
        print(nome, 'nasceu no ano de', ano, " voce tem mais de 17 anos")
    else:
        print(nome, 'nasceu no ano de', ano, " voce nao tem mais de 17 anos")


print("inicio do programa")

Idade()

#tabuada 9
f= open("tabuada9teste.txt", "w")
for i in range (0, 11):
    f.write("9x"+ str(i) + "=" + str(i*9) + " ")
f.close()

f= open("tabuada9teste.txt", "r")
print(f.read())
f.close()

#dados
nome = input("insira seu nome")
rg = int(input("insira seu rg"))
cpf = int(input("insira seu cpf"))
ano_nasc = int(input("insira seu ano de nascimento "))

rg = str(rg)
cpf = str(cpf)
idade = str(2021-ano_nasc)
ano_nasc = str(ano_nasc)

f= open("dados.txt", "w")
f.write("nome "+ nome +"\n")
f.write("RG= " + rg + "\n")
f.write("CPF= " + cpf + "\n")
f.write("ano de nascimento=" + ano_nasc + "\n")
f.write("idade " + idade +" anos" + "\n")
f.close()

f= open("dados.txt", "r")
print(f.read())
f.close()

#---

arq = input("insira o nome do arquivo txt= ")
arq = arq + ".txt"

print(arq)

f = open(arq, "r")
for linha in f:
    print(linha.split())
f.close()

nome = input("nome do aluno: ")
nota1 = float(input("informe a 1ª nota"))
nota2 = float(input("informe a 2ª nota"))
media = (nota1+nota2)/2

nome = str(nome)
nota1 = str(nota1)
nota2 = str(nota2)

if media >= 6:
    sit = "aprovado"
elif media < 6:
    sit = "reprovado"

media = str(media)

f= open("nota.txt", "w")
f.write("nome "+ nome + "\n")
f.write("media final= "+ media + "\n")
f.write("situaçao "+ sit + "\n")
f.close()

f= open("nota.txt", "r")
print(f.read())
f.close()
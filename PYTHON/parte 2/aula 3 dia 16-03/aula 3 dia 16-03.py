#abrindo arquivo nfl
arquivo = open("arquivo_jogadoresNFL.txt", "r")
print(arquivo)
print(arquivo.read())


#criando e escrevendo arquivo
f= open("teste.txt", "w")
f.write("texto 1")
f.close()
#lendo
f= open("teste.txt", "r")
print(f.read())
f.close()

#criando e lendo com with
with open("teste.txt", "w") as f:
    f.write("texto 1\n")
    f.write("texto 2")
#lendo o arquivo
with open("teste.txt", "r") as f:
    print(f.read())

with open("teste.txt", "a") as f:
    f.write("\ntexto 3")

print("lendo linha a linha")
f = open("arquivo_teste.txt", "r")
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline(5)) # 5 define o numeros e caracteres a ser lido dessa linha

print("transforma o arquivo em uma lista")
f = open("arquivo_teste.txt", "r")
print(f.readlines())
f.close()

# ler todas as linhas com for
f = open("arquivo_teste.txt", "r")

for linha in f:
    print(linha)
f.close()

# Ler as linhas de um arquivo com o for e separar as palavras de cada linha com o método split
# transforma cada uma das linha em listas separadas
f = open("arquivo_teste.txt", "r")
for linha in f:
    print(linha.split())
f.close()

# Abrir um arquivo txt e escrever elementos de uma lista

f = open("arquivo_escrever.txt", "w+")

texto = ["palavra 1", "palavra 2", "palavra 3"]

for linha in texto:
    f.write(linha)
    f.write("\n")
f.close()

# ler um arquivo com caracteres acentuados:

f = open("arquivo_portugues.txt", "r")

print(f.read())
f.close()

f = open("arquivo_portugues.txt", "r", encoding="utf-8")

print(f.read())
f.close()


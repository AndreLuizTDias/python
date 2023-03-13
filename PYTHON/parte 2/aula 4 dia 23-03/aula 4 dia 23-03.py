nome = "carol maria"
print(nome[1])
#imprimindo nome
for i in nome:
    print(i)

for i in range(len(nome)):
    print(nome[i])

print("slicing em string resultado rol m")
print(nome[2:7])
print(nome[:7])
print(nome[2:])

nome = "ola mundo!"
print(nome[1::2]) # mostras os caracteres no indice impares
print(nome[::2])# mostra os caracteres no indice pares

print(nome[::-1])# inverte a palavra

print("="*50)
#substitui determinada string por outra string
nome = "carol maria"

nome1 = nome.replace("carol", "aurora")
print(nome1)

print("="*50)
#nome letra maiuscula/ minuscula
nome = "Carol Maria"

print(nome.upper()) #maiusculo dentro do print
nome1 = nome.upper() #maiusculo
print(nome1)

nome1 = nome.lower() #minusculo
print(nome1)

print("="*50)
#caítalizar a 1ªletra da string

nome = "lucas foi merendar na casa da tia"

print(nome.capitalize())

print("{:_>10}".format("teste"))


print("=="*30)
print("tipos de set")
print("=="*30)

a = {1, 2, 2, 4, 4}
b = set()

print("set a", a)
print("tamanho da set a=", len(a))

a1 = set("python")
print(a1)

print("=="*30)
print("lendo o set com for ")
print("=="*30)
a2= {5, 98, 948, 1, 5}

for i in a2:
    print("a2:", i)

print("=="*30)
print("inserindo elemento set")
print("=="*30)

a3 = {1, 2}
a3.add(3)
print("add 3 ao set", a3)

a3.remove(1)
print("removi o numero 1 do set", a3)

a.discard(1)
print("tentei remover o 1 denovo so que ele nao existe, com o discard o pyhon nao da erro se tentar remove algo que nao existe", a3)

print("=="*30)
print("uni set ")
print("=="*30)

b1 = {8, 7}
c1 = {11,10}

d1 = a3 | b1
print("uni a3+b1", d1)

d1 = a3 | b1 | c1
print("uni a3+b1+c1", d1)

print("union so uni dois set", a3.union(b1))


print("=="*30)
print("interçao de set")
print("=="*30)

nome = {"andre","luiz","dias"}
nome1 = {"andre", "dias", "trigueiro"}

print(nome.intersection(nome1))
print(nome-nome1)
print("traz elementos que nao sao comuns entre os dois", nome ^ nome1)
print(nome.symmetric_difference(nome1))

print("verifica se nao existe elementos em comum entre os dois conjuntos= ", nome.isdisjoint(nome1)) #verifica se tem tem elementos diferente nos conjuntos

print("=="*30)
print("verifica elementos")
print("=="*30)

nome = {"andre", "luiz", "dias"}
nome1 = {"andre", "dias", "trigueiro"}

print(("andre" and "dias") in nome)
print(("andre" and "dias") not in nome)

print("verifica se tem todos os elemens de nome em nome1= ", nome.issubset(nome1))
print("verifica se um conjunto e igual ou maior que o outro ", nome.issuperset(nome1))

print("transforma um conjunto em lista")
nome = list(nome)
print(nome[0])

print("transforma um conjunto em tupla")

nome1 = tuple(nome1)
print(nome1[0])



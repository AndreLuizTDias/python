class pessoa():
    pass


pessoa1 = pessoa()
pessoa1.nome = "Juliana"
pessoa1.idade = 23
pessoa1.peso = 75
print(pessoa1.nome, pessoa1.idade, pessoa1.peso)

pessoa2 = pessoa()
pessoa2.nome = "Carlos"
pessoa2.idade = 39
pessoa2.peso = 72
print(pessoa2.nome, pessoa2.idade, pessoa2.peso)

print("=" * 30)


class pessoa(object):
    def __init__(self):
        self.nome = "juliana"
        self.idade = 23
        self.peso = 75


pessoa1 = pessoa()
print(pessoa1.nome, pessoa1.idade, pessoa1.peso)

print("=" * 30)

# forma mais comum de criar classes|| metodos


class pessoa(object):
    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso
    def andar(self):#metodos andar
        print("o ser humano e um mamifero que anda")


pessoa1 = pessoa("juliana", 23, 75)
pessoa2 = pessoa("Carlos", 39, 72)

pessoa1.andar()
pessoa2.andar()

print("="*30)
print("calculadora")

class calculadora:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def soma(self):
        return self.a + self.b
    def subtrai(self):
        return self.a - self.b
    def multiplica(self):
        return self.a * self.b
    def divide(self):
        return self.a / self.b

c = calculadora(150, 2)
print('soma:', c.soma())
print('subtraçao:', c.subtrai())
print('multiplicaçao', c.multiplica())
print('divisão', c.divide())

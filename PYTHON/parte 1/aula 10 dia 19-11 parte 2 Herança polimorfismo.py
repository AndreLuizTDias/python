#HERANÇA
class pessoa(object):
    def __init__(self, nome, cpf, ano):
        self.nome = nome
        self.cpf = cpf
        self.ano_nasc = ano

class aluno(pessoa):
    def __init__(self, nome, cpf, ano):
        super().__init__(nome, cpf, ano)

class professor(pessoa):
    def __init__(self, nome, cpf, ano):
        super().__init__(nome, cpf, ano)

aluno1 = aluno("juliana", 123456789, 1998)
print(aluno1.nome, aluno1.cpf, aluno1.ano_nasc)

#polimorfismo

class pessoa(object):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class pessoafisica(pessoa):
    def __init__(self, cpf, nome, idade):
        pessoa.__init__(self, nome, idade)
        self.cpf = cpf


class pessoajuridica(pessoa):
    def __init__(self, cnpj, nome, idade):
        pessoa.__init__(self, nome, idade)
        self.cnpj = cnpj

pessoafisica1 = pessoa(123456789-1, "andre", 22)

print(pessoafisica1.cpf, pessoafisica1.nome, pessoafisica1.idade)

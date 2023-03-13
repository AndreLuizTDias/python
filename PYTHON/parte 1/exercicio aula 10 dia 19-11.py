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

num1 = float(input("informe um numero: "))
num2 = float(input("informe um numero: "))

res = calculadora(num1, num2)

print("soma", res.soma(), "subtraçao", res.subtrai(), "multiplicaçao", res.multiplica(), "divisao", res.divide())


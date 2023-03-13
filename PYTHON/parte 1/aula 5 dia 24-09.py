
print("nome {0} e idade {1}".format('python', 25))

for i in range (1,11):
    print('{0} {1} {2}'. format(i, i*i, i*i*i))

for i in range (1,11):
    print('{0:>2} {1:>3} {2:>4}'. format(i, i*i, i*i*i))

frase = 'testando format'

print("{0:>20}".format(frase))

print("{0:#>20}".format(frase))

print("{0:^20}".format(frase))

print("{0:.6}".format(frase))

print("{:>10}".format("teste"))

print("{:_>10}".format("teste"))

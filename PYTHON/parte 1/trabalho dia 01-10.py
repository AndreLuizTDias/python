

multi4 = 0

for i in range (1,101):
    if (i % 4 == 0):
        print(i,"e multiplo de 4", sep="-")
        multi4 += 1

multi4 = 0
qtde = 0
for i in range (1,101):
    if (i % 4 == 0):
        print(i,"e multiplo de 4", end=' | ')
        multi4 += 1
        qtde += 1

print("quantidade de multiplos de 4= ", qtde)

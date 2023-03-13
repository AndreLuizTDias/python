n1 = int(input("informe o primeiro numero "))
n2 = int(input("informe o segundo numero "))

soma = n1+n2
subt = n1-n2
mult = n1*n2
divs = n1/n2

soma = str(soma)
subt = str(subt)
mult = str(mult)
divs = str(divs)

a = open("minicalc.txt", "w")
a.write("soma dos numeros inseridos = " + soma + "\n")
a.write("subtraçao dos numeros inseridos = " + subt + "\n")
a.write("multiplicaçao dos numeros inseridos = " + mult + "\n")
a.write("divisao dos numeros inseridos = " + divs + "\n")
a.close()

a = open("minicalc.txt", "r")
print(a.read())
a.close()

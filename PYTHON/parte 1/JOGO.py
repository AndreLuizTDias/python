

lista1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
          'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in range(0, 6):
    n1= int(input("informe o numero"))
    if 0 <= n1 <= 4:
        print(lista1[n1*5])
    elif 4 < n1 <= 11:
        print(lista1[n1+4])
    elif 11 < n1 <= 16:
        print(lista1[n1+2])
    elif 16 < n1 <= 20:
        print(lista1[n1+3])
    elif 20 < n1 <= 25:
        print(lista1[n1])
    else:
        print("numero inserido invalido, reinicie o programa")







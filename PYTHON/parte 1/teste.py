def cubo():

    lista1 = []
    lista2 = []

    for i in range(0, 5):
         lista1.append(int(input("insira um numero: ")))

    lista1.sort()
    for i in range(0,5):
         lista2.append(lista1[i]**3)

    print("valores inseridos: ",lista1)
    print("cubo dos numeros inserido", lista2)

    print("soma do cubo de todos os elementos da lista:",sum(lista2))
    print("maior valor", max(lista2))
    print("menor valor", min(lista2))

cubo()

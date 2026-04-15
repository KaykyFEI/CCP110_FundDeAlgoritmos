from random import randint

M = []

for linha in range(10):
    lista = []
    for coluna in range(15):
        lista.append(randint(0, 100))
    M.append(lista)

for linha in range(len(M)):
    for coluna in range(len(M[linha])):
        print("%3d" % M[linha][coluna], end = " ")
    print()

for linha in range(10):
    print("%3d" % M[linha][0])
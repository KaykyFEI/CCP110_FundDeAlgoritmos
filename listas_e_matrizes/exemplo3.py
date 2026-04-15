M = []

for linha in range(10):
    lista = []
    for coluna in range(15):
        lista.append(linha+coluna)
    M.append(lista)

for linha in range(10):
    for coluna in range(15):
        print(" | " + "%2d" % M[linha][coluna] + " | ", end = " ")
    print("\n----------------------------------------------------------------------------------------------------------------------------------------")
# ler o arquivo pares.txt
pares = open("pares.txt", "r")

multiplos4 = open("multiplos_4.txt", "w")

for linha in pares.readlines():
    if int(linha) % 4 == 0:
        multiplos4.write(linha)

pares.close()
multiplos4.close()
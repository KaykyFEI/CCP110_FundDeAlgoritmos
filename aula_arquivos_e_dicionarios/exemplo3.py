par = open("pares.txt", "w")
impar = open("impar.txt", "w")

for n in range(1000):
    if n % 2 == 0:
        par.write(str(n) + "\n")
    else:
        impar.write(str(n) + "\n")

par.close()
impar.close()
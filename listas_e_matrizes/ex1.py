from random import randint
from random import uniform

# Inteiros: a primeira lista com 10 números inteiros gerados aleatoriamente

inteiros = []

for i in range(10):
    numero_aleatorio = randint(1, 100)
    inteiros.append(numero_aleatorio)

# print(inteiros)

# Reais: a segunda lista com 15 números reais gerados aleatoriamente
reais = []

for i in range(15):
    numero = round(uniform(1, 100), 1)
    reais.append(numero)

# print(reais)

# Strings: A terceira lista com 7 strings criadas por você
strings = []
strings.append("aa")
strings.append("bb")
strings.append("cc")
strings.append("dd")
strings.append("ee")
strings.append("ff")
strings.append("gg")
strings.append("hh")

# print(strings)

completa = [inteiros, reais, strings]
inteiros = []
reais = []
strings = []

for i in range (50):
    completa[0].append(randint(1, 100))

print(completa)
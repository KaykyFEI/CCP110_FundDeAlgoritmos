T = [11, 7, 2, 4]

menor_valor = T[0]

for valor in T:
    if valor < menor_valor:
        menor_valor = valor
        
print(menor_valor)
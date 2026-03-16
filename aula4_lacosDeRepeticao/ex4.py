"""
Faça um programa que leia 6 números inteiros positivos do usuário e
exiba o maior número lido.
"""
maior = 0
for x in range(0, 6):
    n = int(input("Digite um número: "))
    if maior < n:
        maior = n

print(f"O maior número é: {maior}")
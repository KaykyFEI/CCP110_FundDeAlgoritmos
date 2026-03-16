"""
Escreva um programa que imprima a tabuada de um número digitado
pelo usuário
"""
numero = int(input("Digite um número: "))

for x in range(1, 11, 1):
    x = x * numero
    print(x)
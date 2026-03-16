""" 
Faça um programa que imprima os números pares entre 0 e um
número digitado pelo usuário.
"""
x = 1
numero = int(input("Digite um número: "))

while x < numero:
    if (x % 2) == 0:
        print(x)
    x = x + 1
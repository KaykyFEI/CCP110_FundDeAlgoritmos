"""
Faça um programa que leia um valor n, inteiro e positivo, calcule e
mostre a seguinte soma:

"""
valor = int(input("Digite um valor inteiro e positivo: "))
valor = valor + 1
soma = 0

for i in range(1, valor ,1):
    fracao = 1 / i
    soma = soma + fracao

print(f"A soma é: {soma:.2f}")
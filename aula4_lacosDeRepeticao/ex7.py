"""
Faça um programa para calcular a somatória de 10 números
• Os números devem ser digitados pelo usuário
• Será necessário um contador para controlar o número de repetições
• e um acumulador para acumular a soma dos números entre cada
repetição
"""
n = 0
somatoria = 0

for i in range(0, 11, 1):
    n = int(input("Digite um núm2ero: "))
    somatoria = somatoria + n 

print(f"A somatória dos números digitados é: {somatoria}")
"""
Escreva um programa que lê dois números:
• Então, seu programa deve perguntar qual a operação deseja realizar.
– As opções são:
¨ soma(+)
¨ subtração(-)
¨ multiplicação(ˆ)
¨ divisão(/)
• Exiba o resultado da operação escolhida . . .
– ou uma mensagem dizendo que a operação escolhida não é válida.
"""

n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
operacao = input("Digite a operação desejada (+ | - | * | /): ")

if operacao == "+":
    resultado = n1 + n2
elif operacao == "-":
    resultado = n1 - n2
elif operacao == "*":
    resultado = n1 * n2
elif operacao == "/":
    resultado = n1 / n2
else:
    resultado = "Operação inválida: " + operacao

print(resultado)
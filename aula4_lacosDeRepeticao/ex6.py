"""
Escreva um programa que leia números digitados pelo usuário:
• O programa deve ler os números até que o 0 (zero) seja digitado.
• Quando o 0 for digitado, o programa deve exibir:
– a quantidade de números que foram digitados;
– a somatória destes números;
– e a média aritmética.
"""
qtdNum = 0
n = 0
somatoria = 0

while True:
    n = int(input("Digite um número: "))
    if n != 0:
        qtdNum = qtdNum + 1
        somatoria = somatoria + n
    else:
        mediaAritmetica = somatoria / qtdNum
        break

print(f"A quantidade de números que foram digitados é: {qtdNum}.")
print(f"A somatória desses números é: {somatoria}.")
print(f"A média aritmética dos números digitados é: {mediaAritmetica}.")
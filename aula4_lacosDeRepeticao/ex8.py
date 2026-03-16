"""
Calcular a somatória de valores digitados pelo usuário:
• Continue somando até que o número 0 (zero) seja digitado.
• Quando o 0 for digitado o resultado da somatória é exibido.
"""
somatorio = 0

while True:
    numero = int(input("Digite um número: "))
    if numero != 0:
        somatorio = somatorio + numero
    else:
        print(f"A soma dos números digitados é: {somatorio}")
        break
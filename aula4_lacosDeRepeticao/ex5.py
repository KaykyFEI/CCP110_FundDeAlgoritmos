"""
Faça um programa que solicita um número entre 0 e 10:

Mostre uma mensagem de erro caso o valor seja inválido e continue
pedindo até que o usuário informe um valor válido.

Quando o valor for válido dê a mensagem “número aceito”.

Dica: você pode utilizar operadores lógicos (and ou or) na condição do
while também!
"""
while True:
    numero = int(input("Digite um valor entre 0 e 10: "))
    if (numero >= 0) and (numero <= 10):
        print(f"O número {numero} é aceito.")
        break
    else:
        print(f"O número {numero} é inválido.\n")
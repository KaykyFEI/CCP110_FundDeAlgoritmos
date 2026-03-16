"""
Foi feita uma pesquisa entre os habitantes de uma região. Foram coletados
os dados de idade, sexo (M/F) e salário. Faça um programa que informe:
• a média de idade do grupo;
• a média de salários dos homens;
• quantidade de mulhoeres com salário abaixo de R$600,00
Encerre a entrada de dados quando for digitada uma idade negativa (os
dados da idade negativa não podem entrar nos cálculos dos itens
solicitados acima).
"""
contadorSexo = 0
contadorSexoHomem = 0
salarioHomens = 0
salarioMulheres = 0
salarioBaixoMulheres = 0
somaIdade = 0
mediaIdade = 0
contadorIdade = 0

while True:
    idade = int(input("Digite a idade do indivíduo: "))
    if idade < 0:
        print("Idade inválida. Inicie o programa novamente.")
        break
    contadorIdade += 1
    somaIdade += idade
    # Média de idade do grupo
    mediaIdade = somaIdade / contadorIdade

    sexo = input("Digite o sexo do indivíduo (M / m / F / m): ")
    while sexo != "M" and sexo != "m" and sexo != "F" and sexo != "f":
        sexo = input("Digite um valor válido: ")

    contadorSexo += 1

    if sexo == "M" or sexo == "m":
        contadorSexoHomem += 1

    salario = float(input("Digite o salário do indivíduo: "))
    while salario < 0:
        salario = float(input("Digite um valor acima de R$ 0,00: "))
    
    if sexo == "M" or sexo == "m":
        salarioHomens += salario
    else:
        salarioMulheres += salario
        # Armazena a quantidade de mulheres que recebem menos que 600 reais.
        if salario < 600:
            salarioBaixoMulheres += 1


    # Calcula a média de salários dos homens
    mediaSalariosHomens = salarioHomens / contadorSexoHomem


# Impressão de dados

print(f"A média de idade de grupos é {mediaIdade} anos.")
print(f"A média de salários de homens é R$ {mediaSalariosHomens:.2f}.")
print(f"A quantidade de mulheres com salário abaixo de R$ 600,00 são {salarioBaixoMulheres}.")
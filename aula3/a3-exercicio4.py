"""
A empresa X resolveu conceder um aumento de salário a seus
funcionários de acordo com a tabela abaixo:
Salário Percentual de Reajuste
0 - 400.00 15%
400.01- 800.00 12%
800.01- 1200.00 10%
1200.01 - 2000.00 7%
Acima de 2000.00 4%
Leia o salário do funcionário e calcule e mostre o novo salário, bem como o
valor de reajuste ganho e o índice reajustado, em percentual.
"""
salario = 0
valorReaj = 0
salarioReaj = 0
# Declaração das variáveis de reajuste
rj1 = 15
rj2 = 12
rj3 = 10
rj4 = 7
rj5 = 4

salario = float(input("Digite o seu salário: "))

# Condições de 
if salario < 0:
    print(f"O valor {salario} é inválido.")
else:
    if salario <= 400.00:
        percentual = rj1
    elif salario <= 800.00:
        percentual = rj2
    elif salario <= 1200.00:
        percentual = rj3
    elif salario <= 2000.00:
        percentual = rj4
    else:
        percentual = rj5

decimalIndice = percentual / 100
valorReaj = salario * decimalIndice
salarioReaj = salario + valorReaj


print(f"O seu salário reajustado é: R$ {salarioReaj:.2f}")
print(f"O valor do reajuste foi: R$ {valorReaj:.2f}")
print(f"O índice do reajuste foi: {percentual:.0f}%")
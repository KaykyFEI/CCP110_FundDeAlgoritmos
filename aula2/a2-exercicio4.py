salario = float(input("Digite o seu salário e o programa retornará o seu novo salário:\n"))
novoSalario = 0.0

if salario <= 1250.0:
    novoSalario = salario*1.15
else:
    novoSalario = salario*1.10

print(f"O seu novo salário é {novoSalario:.2f}")
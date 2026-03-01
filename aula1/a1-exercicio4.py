salarioHora = float(input("Digite o valor da hora de trabalho: "))
horasMes = int(input("Digite o número de horas trabalhadas no mês: "))

salarioBruto = salarioHora*horasMes
impostoDeRenda = salarioBruto*0.11
inss = salarioBruto*0.08
sindicato = salarioBruto*0.05
salarioLiquido = salarioBruto - impostoDeRenda - inss - sindicato

print("+ Salário Bruto: R$ %.2f" % salarioBruto)
print("- IR (11%): R$ %.2f" % salarioBruto)
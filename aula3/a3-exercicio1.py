nota1Aluno = float(input("Digite a sua primeira nota: "))
nota2Aluno = float(input("Digite a sua nota: "))

mediaNotas = (nota1Aluno + nota2Aluno) / 2

if mediaNotas < 5:
    print("Reprovado.")

# Elif é igual else + if
elif mediaNotas == 10:
    print("Aprovado com Distinção.")
else:
    print("Aprovado")
"""
Elaborar um programa que leia um conjunto de valores reais,
correspondentes a 80 notas dos alunos de uma turma, notas estas que
variam de 0 a 10. Calcule o mostre:
• a quantidade de alunos aprovados (nota >= 6,0)
• a média das notas da turma;
"""
media = 0
aprovados = 0
notas = 0
alunos = 0

for i in range(0, 80, 1):
    nota = float(input("Digite uma nota de 0 a 10: "))
    alunos = alunos + 1
    if nota >= 6:
        aprovados = aprovados + 1
    notas = notas + nota

media = notas / alunos

print(f"A quantidade de alunos aprovados é: {aprovados}.")
print(f"A média da turma é: {media:.2f}.")
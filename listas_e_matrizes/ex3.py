""" Faça um programa para receber uma matriz 3 x 3 (solicitar ao usuário)
Apresentar a soma dos elementos da diagonal principal """

M = []

for linha in range(3):
    lista = []
    for coluna in range(3):
        lista.append(int(input(f"Linha {linha + 1}. Digite um número: ")))
    M.append(lista)

soma = 0

for linha in range(len(M)):
    for coluna in range(len(M[linha])):
        if linha == coluna:
            soma = soma + M[linha][coluna]
            
print(soma)
""" Um jogo da velha digital guarda as pontuações de cada casa em uma matriz 3x3. Precisamos criar um algoritmo para somar apenas os pontos que estão na diagonal principal do tabuleiro
.
Sua Tarefa:
Declare uma matriz 3x3 já preenchida no seu código (Exemplo: tabuleiro = [
,
,
])
.
Crie uma variável soma_diagonal iniciando em 0.
Crie um único laço de repetição for i in range(3): (este i servirá tanto como índice da linha quanto da coluna simultaneamente!).
Dentro do laço, acesse o elemento da diagonal principal escrevendo tabuleiro[i][i] e adicione esse valor à variável soma_diagonal.
Fora do laço, imprima o resultado final da soma. """

# declaração de uma matriz já preenchida
tabuleiro = [[1,2,3], [3,2,1], [1,1,1]]

# variável para armazenar o valor da soma
soma_diagonal = 0

for i in range(3):
    soma_diagonal += tabuleiro[i][i]
    
print(soma_diagonal)
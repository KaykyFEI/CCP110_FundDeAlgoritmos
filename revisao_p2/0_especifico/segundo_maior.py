# prática de exercício para pegar o segundo maior número inserido num programa

""" Um clube de atletismo está registrando as distâncias dos saltos dos atletas durante um treino. O treinador precisa saber rapidamente qual foi o salto mais longo (medalha de ouro) e o segundo salto mais longo (medalha de prata).
Sua Tarefa:
Crie duas variáveis, maior e segundo_maior, e inicie ambas com o valor 0.
Crie um laço de repetição infinito (usando while True
).
Dentro do laço, peça para o usuário digitar a distância do salto (como float). Se o usuário digitar 0, utilize o comando break para encerrar o laço imediatamente
.
Crie a lógica condicional:
Se o novo salto digitado for maior que a variável maior, a variável segundo_maior deve receber o valor antigo de maior, e a variável maior deve ser atualizada com o novo salto.
Caso contrário (se não for o maior de todos), verifique se o salto é maior que o segundo_maior. Se for, atualize apenas o segundo_maior.
Fora do laço de repetição, imprima na tela o maior e o segundo maior valor. """

maior_salto = 0
segundo_maior_salto = 0

while True:
    novo_salto = float(input("Digite a distância do salto ou 0 para encerrar o programa: "))
    if novo_salto == 0: # estava na última condição. Colocado como primeira para evitar processamento desnecessário com o 0
        break
    elif novo_salto > maior_salto:
        segundo_maior_salto = maior_salto
        maior_salto = novo_salto
    elif novo_salto > segundo_maior_salto:
        segundo_maior_salto = novo_salto
        
    # continue -> desnecessário pois o while True continua o laço automaticamente

print(f"A maior distância de salto foi {maior_salto} metros")
print(f"A segunda maior distância de salto foi {segundo_maior_salto} metros")
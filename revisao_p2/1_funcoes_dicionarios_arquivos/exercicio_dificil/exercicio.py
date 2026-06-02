""" A escola agora quer processar as notas das provas. Existe um arquivo chamado notas.txt que guarda o nome do aluno e suas três notas separadas por ponto e vírgula, neste exato formato: Nome;Nota1;Nota2;Nota3 (Exemplo: Ana;8.5;9.0;7.5).
Sua Tarefa: Crie uma função chamada calcular_medias().
A função deve abrir e ler as linhas do arquivo notas.txt
.
Separe os dados de cada linha utilizando o delimitador correto
.
Converta as três notas de string para números decimais (float)
.
Calcule a média aritmética simples das 3 notas de cada aluno.
Crie, preencha e retorne (return) um dicionário onde a chave é o nome do aluno e o valor é a sua média final calculada
. """

# declaração da função para calcular as médias das notas
def calcular_medias():
    # declaração do dicionário que será retornado ao fim da função
    aluno_media = {}
    
    # abre o arquivo notas.txt no modo leitura. Método with open tem o seu fechamento automático
    with open("notas.txt", "r") as arquivo:
        # itera sobre cada linha do arquivo usando o readlines()
        for aluno in arquivo.readlines():
            # para cada linha, limpa \n (quebra-linha) da lista e separa os itens pelo delimitador ;
            lista_limpa = aluno.strip().split(";")
            # atribui o nome do aluno à uma variável
            nome = lista_limpa[0]
            # primeiro transforma as notas de string para float -> soma as 3 -> divide por 3 (média aritmética) -> atribui o resultado à variável "media"
            media = (float(lista_limpa[1]) + float(lista_limpa[2]) + float(lista_limpa[3])) / 3
            # arrendonda o valor da média considerando somente duas casas decimais
            media_arredondada = round(media, 2)
            # inseri o nome do aluno e sua média arrendondada no dicionário
            aluno_media[nome] = media_arredondada
    # retorna o dicionário para como resposta da função
    return(aluno_media)

medias_calculadas = calcular_medias()
print(medias_calculadas)
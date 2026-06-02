""" O sistema foi desligado e o dicionário da memória foi apagado. Agora, quando o programa iniciar, a secretária precisa carregar os dados que foram gravados no arquivo de texto de volta para um dicionário no Python, para que ela possa consultá-los.
Sua Tarefa: Escreva uma função chamada carregar_idades().
A função não recebe parâmetros, mas deve abrir o arquivo idades.txt em modo de leitura
.
Leia as linhas do arquivo. Para cada linha, separe o nome e a idade usando o caractere separador adequado
.
Armazene esses dados em um novo dicionário (a chave é o nome, o valor é a idade). Atenção: lembre-se de que tudo lido de um arquivo é string e possui a quebra de linha \n embutida
. Você precisará limpar isso e converter a idade para número inteiro
.
Feche o arquivo e retorne (return) o dicionário criado. """

def carregar_idades():
    dicionario_interno = {} # cria o dicionário local
    with open("idades.txt", "r") as arquivo: # abre o arquivo de persistencia dos dados
        for linha in arquivo: # iteração de leitura para cada linha do arquivo
            if "-" in linha:
                nome, idade = linha.strip().split("-", 1) # retira os espaços em branco e separa os dados pelo "-"
                dicionario_interno[nome.strip()] = int(idade.strip()) # atribui a chave e o valor para o dicionario local
    # arquivo.close() -> não é necessário com o gerenciador de contexto "with open..."
    return dicionario_interno # retorna o dicionario interno como resposta da função
    
print(carregar_idades())
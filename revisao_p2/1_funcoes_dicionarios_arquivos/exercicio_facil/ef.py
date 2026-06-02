# Exercício de revisão gerado pelo NotebookLM para a prova final de fundamentos de algoritmos.
# Eles foram criados utilizando os slides das aulas como fonte. Nenhum conteúdo externo.

# Exercício de nível fácil para o assunto "Funções, Dicionários e Arquivos"
""" A secretaria de uma escola precisa registrar as idades dos alunos. Atualmente, a secretária coleta esses dados em um dicionário no Python (exemplo: {"Ana": 22, "Carlos": 25}), mas percebeu que perde todas as informações quando o programa é encerrado, pois a memória não é permanente
. Ela precisa de uma solução que grave essas informações em um arquivo de texto, garantindo que os novos registros não apaguem os alunos salvos em dias anteriores
.
Sua Tarefa: Escreva uma função chamada salvar_idades(dicionario).
A função deve abrir um arquivo chamado idades.txt no modo adequado para adicionar dados sem sobrescrever o conteúdo existente
.
Itere sobre o dicionário recebido e grave cada registro no arquivo exatamente no formato: Nome - Idade (lembre-se de incluir a quebra de linha \n ao final)
.
Feche o arquivo ao final para garantir que o Sistema Operacional salve os dados corretamente
. """

# Dicionário é uma estrutura de dados que tem chave-valor. Portanto, para cada chave, será atribuído um valor. A chave pode ter o nome que quiser.

def salvar_idades(dicionario):
    # abrindo com o modo escrita preservando o conteúdo já existente
    arquivo = open("idade.txt", "a")
    
    # iteração nos itens do dicionário para registrar no arquivo persistente
    for nome, idade in dicionario.items():
        # método "write" para escrever o dicionário no arquivo
        arquivo.write(f"{nome} - {idade}\n")
    arquivo.close()

# criacao do dicionario alunos
alunos = {}

print("Salvar nova idade de aluno.")
nome = input("Digite o nome do aluno: ")
idade = int(input("Digite a idade do aluno: "))
alunos[nome] = idade

salvar_idades(alunos)

print("Salvo com sucesso.")
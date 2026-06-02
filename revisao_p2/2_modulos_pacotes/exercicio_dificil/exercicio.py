""" Agora o hospital recebe os dados dos pacientes de um sistema antigo que exporta as informações em uma única linha de texto extremamente bagunçada e com a unidade de medida colada no número. Exemplo de entrada: "  Carlos Silva ; hoMem ; 75.5kg  ".
Sua Tarefa:
No arquivo regras.py, crie uma nova função chamada processar_registro(linha).
Essa função deve separar a string pelo delimitador correto
.
Limpe os espaços em branco do nome e do sexo
.
Isole o peso numérico usando o método replace("kg", "") para retirar o texto "kg" e, em seguida, converta-o para float
.
Utilize as suas funções anteriores (padronizar_texto e pode_doar) para verificar se este paciente pode doar sangue.
A função deve retornar uma string formatada usando o estilo clássico de marcadores (%s) exigido na sua disciplina
, exatamente neste padrão: "CARLOS SILVA: Apto" ou "CARLOS SILVA: Inapto".
Bônus Técnico: No final do arquivo regras.py, insira o bloco if __name__ == "__main__":
 e faça um teste local da função passando a string "  Carlos Silva ; hoMem ; 75.5kg  ", imprimindo o resultado na tela.
 """

# importa a função pode_doar do módulo regras
from regras import pode_doar, padronizar_texto, processar_registro

linha = input("Insira a linha de dados do antigo sistema: ")


processar_registro(linha)
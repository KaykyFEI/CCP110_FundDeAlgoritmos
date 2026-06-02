""" Um hospital precisa de um pequeno sistema para verificar se um paciente está apto a doar sangue baseado em uma regra simples de peso. Para que outros sistemas do hospital possam reaproveitar essa lógica no futuro, a diretoria de TI exigiu que a função ficasse separada em um arquivo de módulo
. A regra de negócio é: Mulheres precisam ter no mínimo 50 kg e Homens no mínimo 60 kg
.
Sua Tarefa: Você precisará escrever o código de dois arquivos separados:
Arquivo regras.py (O Módulo): Escreva uma função chamada pode_doar(sexo, peso) que retorne True se a pessoa puder doar e False caso contrário
.
Arquivo principal.py: Escreva o código que importa o seu módulo regras. O programa deve perguntar o sexo e o peso do usuário, usar a função importada e imprimir na tela se ele pode ou não doar sangue
. """

# importa a função pode_doar do módulo regras
from regras import pode_doar, padronizar_texto

sexo = input("Digite o sexo do paciente (Homem | Mulher): ")
peso = float(input("Digite o peso do paciente: "))

sexo = padronizar_texto(sexo)

resultado = pode_doar(sexo, peso)

if resultado:
    print("Pode doar sangue.")
else:
    print("Não pode doar sangue.")
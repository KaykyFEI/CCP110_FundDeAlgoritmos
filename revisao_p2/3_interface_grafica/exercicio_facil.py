""" A biblioteca da universidade precisa de uma tela inicial simplificada para seu novo sistema de totens de autoatendimento. Os alunos precisam ver uma tela amigável antes de começarem a interagir com o sistema.
Sua Tarefa: Desenvolva um código em Python utilizando a biblioteca tkinter
. A sua interface gráfica deve conter:
Uma janela principal com um título e tamanho definidos
.
Um Rótulo (Label) exibindo uma mensagem inicial de boas-vindas
.
Um Botão (Button) escrito "Entrar"
.
Uma interação: ao clicar no botão "Entrar", o texto do rótulo de boas-vindas deve ser alterado imediatamente para "Carregando..."
. """

# importa a biblioteca tkinter

from tkinter import *

# cria a janela
janela = Tk()

# titulo da janela
janela.title("Biblioteca FEI")

# define o tamanho da janela
janela.geometry("500x500")

# cria o rótulo exibindo a mensagem de boas-vindas
rotulo = Label(janela, text = "Bem-vindo à biblioteca digital da FEI", font=("Arial Bold", 14))

# configura onde o rótulo vai aparecer na tela
rotulo.place(x=250, y=100, anchor=CENTER)

def clique():
    rotulo['text'] = "Carregando..."

# cria o botão entrar com a ação de mudar texto da label
botao = Button(janela, text="Entrar", command=clique)

# posiciona o botão na janela
botao.place(relx=0.5, rely=0.7, anchor=CENTER)

#função para manter a janela aberto
janela.mainloop()
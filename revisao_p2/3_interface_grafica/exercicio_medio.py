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
. 
Após a tela de boas-vindas, o totem da biblioteca exige que o aluno faça o login no sistema. Precisamos construir essa tela de autenticação.
Sua Tarefa: Desenvolva uma interface gráfica em que o aluno encontre um campo em branco (caixa de texto) para digitar o seu RA (Registro Acadêmico). Abaixo desse campo, deve haver um botão "Login". Quando o aluno clicar nesse botão, o sistema deve exibir uma janela de aviso (message box) na tela com a mensagem: "Login efetuado com sucesso!".
"""

# importa a biblioteca tkinter
from tkinter import *
# importa a função messagebox para criar caixas de texto
from tkinter import messagebox

# cria a janela
janela = Tk()

# titulo da janela
janela.title("Login Totem")

# define o tamanho da janela
janela.geometry("500x500")

# cria o rótulo exibindo a mensagem de boas-vindas
rotulo = Label(janela, text = "Bem-vindo à biblioteca digital da FEI", font=("Arial Bold", 14))

# cria a caixa de texto para inserir o RA
entrada_ra = Entry(janela, width=15, font=("Arial", 14))
entrada_ra.place(relx=0.5, rely=0.6, anchor=CENTER)

# configura onde o rótulo vai aparecer na tela
rotulo.place(x=250, y=100, anchor=CENTER)

def login():
    
    messagebox.showinfo("Aviso", "Login efetuado com sucesso!")

# cria o botão Entrar para fazer login no sistema com o RA
botao = Button(janela, text="Entrar", command=login)

# posiciona o botão na janela
botao.place(relx=0.5, rely=0.7, anchor=CENTER)

#função para manter a janela aberto
janela.mainloop()
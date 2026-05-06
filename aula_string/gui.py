from tkinter import *
from tkinter import messagebox

# cria a janela 
janela = Tk()

# titulo para a janela
janela.title("primeira janela")

# define o tamanho
janela.geometry("600x500")

rotulo = Label(janela, text = "Primeira aplicação gráfica em Python", font=("Arial Bold", 14, ))

rotulo.place(x=300, y=100, anchor=CENTER)

def clique():
    rotulo['text'] = "Novo texto"

botao = Button(janela, text="Clique aqui", command = clique)
botao.place(x = 300, y = 200, anchor=CENTER)


def show():
    res = messagebox.showinfo('Aviso', 'o botao de mensagem foi criado')
    print(res)

botao2 = Button(janela, text="Clique aqui", command=show)
botao2.place(x=300, y=300, anchor=CENTER)

janela.mainloop()
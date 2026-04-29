# sistema de cadastro de pessoas

contatos = open("contatos.txt", "a")

while True:
    nome = input("Digite o nome: ")
    if nome == "":
        break
    telefone = input("Digite o telefone: ")

    contatos.write(f"{nome} {telefone} \n")

contatos.close()
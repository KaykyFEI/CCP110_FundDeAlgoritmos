# funcao que recebe uma lista e retorna a media dos numeros dentro da lista

def media(lista):
    soma = 0
    for num in lista:
        soma += num
    return soma / len(lista)

if __name__ == "__main__":
        print("ola")
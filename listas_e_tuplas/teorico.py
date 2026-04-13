# Cria a lista "Lista" vazia.
Lista = []

# Cria a lista "Lista2" com valores dentro. Importante lembrar que o índice começa em 0.
Lista2 = [2, 5, 7]

print(Lista2[1])

# O ".append" adicione um novo valor no fim da lista "Lista". 
# Adicione "boa noite" no fim de "Lista".
Lista.append("boa noite")
print(Lista)

# Adicione "25 no fim de "Lista".
Lista.append(25)
print(Lista)

# Para alterar o valor de um índice da lista, você chama ela com o índice que deseja alterar e atribui o novo valor
Lista[0] = "bom dia"
print(Lista)

# Para inserir um valor em alguma posição da lista: ".insert(índice, valor)".
Lista2.insert(2, 9)
print(Lista2)

# Para remover um elemento pelo seu índice, utiliza-se ".pop(índice)"
Lista2.pop(1)
print(Lista2)

# Para remover um elemento pelo seu nome, utiliza-se ".remove(nome)"
Lista2.remove(9)
print(Lista2)

# Para calcular o tamanho da lista, utiliz-se "len(lista)". 
# Se quiser retonar o último elemento da lista, pode-se calcular o tamanho da lista e subtrair por 1 e adicionar esse resultado no índice.
print(len(Lista2)-1)

# Para pesquisar numa lista, utiliza-se um laço de repetição. Pode ser while ou for. 

# Em Python, para facilitar, pode utilizar o "if (valor) in (lista)".
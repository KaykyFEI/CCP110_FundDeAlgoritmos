idadeCarro = int(input("Digite a idade do carro em anos: \n"))
carroEstado = ""
if idadeCarro < 3:
    carroEstado = "O seu carro é novo."
else:
    carroEstado = "O seu carro é velho."

print(carroEstado)
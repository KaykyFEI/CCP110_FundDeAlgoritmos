# Variável que irá armazenar os valores obtididos pela função de entrada de dados
altura = int(input("Por favor, digite sua altura em centímetros: "))

# Cálculo para obter o peso ideal
pesoIdeal = (altura*0.727) - 58

# Exibição do peso ideal
print("O seu peso ideal é %.2f kg" % pesoIdeal)
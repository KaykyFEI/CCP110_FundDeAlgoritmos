distanciaAPercorrer = 0
valorCorrida = 0

distanciaAPercorrer = int(input("Digite a distância que deseja percorrer em quilômetros: \n"))

if distanciaAPercorrer > 200:
    valorCorrida = distanciaAPercorrer * 0.45
else:
    valorCorrida = distanciaAPercorrer* 0.50

print(f"O valor final da sua corrida será de R$ {valorCorrida:.2f}.")
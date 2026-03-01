dias = int(input("Digite uma quantidade de dias: "))
horas = int(input("Digite uma quantidade de horas: "))
minutos = int(input("Digite uma quantidade de minutos: "))
segundos = int(input("Digite uma quantidade de segundos: "))

tempoTotal = (dias*86400) + (horas*3600) + (minutos*60) + (segundos*1)

print("O tempo total em segundos foi de %d segundos" % tempoTotal)
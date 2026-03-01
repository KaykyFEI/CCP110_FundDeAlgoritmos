kmPercorridos = float(input("Digite a quantidade de quilômetros percorridos: "))
diasAlugado = float(input("Digite a quantidade de dias que o carro foi alugado: "))

custoAluguel = diasAlugado*60.00
custoKmPercorridos = kmPercorridos*0.15
custoTotal = custoAluguel + custoKmPercorridos

print(custoTotal)
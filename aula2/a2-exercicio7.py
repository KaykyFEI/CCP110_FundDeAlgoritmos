n1 = float(input("Para calcular sua média ponderada, digite sua primeira nota: "))
n2 = float(input("A segunda: "))
n3 = float(input("Por fim, a terceira nota: "))

media = (n1 + (n2*2) + (n3 *3)) / 6

if media < 5:
    print(f"Reprovado. A sua média foi {media:.1f}")
else:
    print(f"Aprovado. A sua média foi {media:.1f}")
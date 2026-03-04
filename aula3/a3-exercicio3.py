"""
Leia 2 valores reais (x e y), que devem representar as coordenadas de
um ponto em um plano.
Então, determine a que quadrante (Q1, Q2, Q3 ou Q4) o ponto pertence
ou se está sobre um dos eixos cartesianos ou na origem (x = y = 0).
"""
x = float(input("Digite o valor de x: "))
y = float(input("Digite o valor de y: "))

if x == 0 and (y > 0 or y < 0):
    qd = "Está sobre o eixo das ordenadas."
elif y == 0 and (x > 0 or x < 0):
    qd = "Está sobre o eixo das abcissas."
elif x > 0 and y > 0:
    qd = "Está no quadrante Q1."
elif x < 0 and y > 0:
    qd = "Está no quadrante Q2."
elif x < 0 and y < 0:
    qd = "Está no quadrante Q3."
elif x > 0 and y < 0:
    qd = "Está no quadrante Q4."
else:
    qd = "Na origem."

print(qd, f"Coordenadas: ({x}, {y})")
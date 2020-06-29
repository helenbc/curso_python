n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
n3 = float(input('Nota 3: '))

p1 = float(input('Peso 1: '))
p2 = float(input('Peso 2: '))
p3 = float(input('Peso 3: '))

mediaPonderada = (n1 * p1 + n2 * p2 + n3 * p3) / (p1 + p2 + p3)

print('Média Ponderada:', mediaPonderada)
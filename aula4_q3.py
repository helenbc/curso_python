#conhecer o valor do boleto e dos juros

boleto = float(input('Digete o valor do boleto: '))
juros = 5/100

#calcular o valor total

valor = boleto + juros * boleto

#mostrar o valor total

print('O valor total é:', valor)
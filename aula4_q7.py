# entrada dos volumes em questao

volumecaixa = float(input("Informe o volume da caixa: "))
volumesapato = float(input("Informe o volume do sapato: "))

# usa-se a divisao inteira pq nao existe sapato pela metade ( não que eu saiba)

quantidadeSapatos = volumecaixa // volumesapato

# quantidades de sapatos 

print('Quantidade de sapatos é:', quantidadeSapatos)
velocidadeMedia = float(input("Informe a velocidade média(Km/h): "))
distancia = int(input("Informe a distância(metros): "))


# para utilizar a distancia recebida, tem que transformar em km ja que na formula usa-se em km

distanciaKm = distancia / 1000

# agora calcular o tempo em horas (padrao formula)

tempoHoras = distanciaKm / velocidadeMedia

# agora transformar o tempo encontrado em horas para minutos - o que a questão pede

tempoMinutos = tempoHoras * 60

print('Quantidade em minutos: ', tempoMinutos)


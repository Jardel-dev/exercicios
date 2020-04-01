#pergunta a distância de uma viagem em km e calcule o preço da passagem, cobrando 0,50 por km de viagem até 200km e 0,45 mais longas
km = float(input('digite a distância da viagem '))
valor = km
if km <= 200:
    km1 = km * 0.50
    print('para essa distancia o valor da passagem é R${:.2f}'.format(km1))
else:
    km2 = km * 0.45
    print('para essa distancia o valor da passagem é R${:.2f}'.format(km2))
#até 80km/h não paga multa, acima de 80 a multa será 7,00 reais por km excedente
vel = int(input('qual é a velocidade do veiculo? '))
if(vel <= 80):
    print('a velocidade de {}km/h é aceitavel nesta rodovia.'.format(vel))
else:
    multa = (vel - 80) * 7
    print('a velocidade de {}km/h ultrapassa o limite de velocidade, a multa será de R${:.2f}'.format(vel, multa))
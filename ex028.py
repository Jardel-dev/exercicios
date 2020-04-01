#acertar um numero aleatório
from random import randint
from time import sleep
computador = randint(1, 5)# computador sorteia de 1 a 5
aleatorio = computador
print('-=-' * 10)
print('vou pensar em um numero entre 1 e 5. tente adivinhar...')
print('-=-' * 10)
jogador = int(input('que numero eu pensei? '))
print('você disse {}'.format(jogador))
print('PROCESSANDO...')
sleep(3)
print('e o computador pensou em {}'.format(aleatorio))
if (aleatorio == jogador):
    print('vc acertou')
else:
    print('vc errou')

#jokenpô
from random import randint
from time import sleep
import playsound
item = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('Suas opções:\n[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA')
playsound.playsound('denovo.mp3')
jogador = int(input('qual é a sua jogada? '))
aleatorio = computador
print(f'Você escolheu {item[jogador]}')
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
print(f'o computador escolheu {item[computador]}')
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('VOCÊ GANHOU')
        playsound.playsound('ganhou.mp3')
    else:
        print('VOCÊ PERDEU')
        playsound.playsound('perdeu.mp3')
elif computador ==1:
    if jogador == 0:
        print('VOCÊ PERDEU')
        playsound.playsound('perdeu.mp3')
    elif jogador == 1:
        print('EMPATE')
    else:
        print('VOCÊ GANHOU')
        playsound.playsound('ganhou.mp3')
elif computador == 2:
    if jogador == 0:
        print('VOCÊ GANHOU')
        playsound.playsound('ganhou.mp3')
    elif jogador == 1:
        print('VOCÊ PERDEU')
        playsound.playsound('perdeu.mp3')
    else:
        print('EMPATE')
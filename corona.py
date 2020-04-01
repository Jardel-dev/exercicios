#codigo que informa se a pessoa está com o virus corona
print('responda o questionário: ')
contato = int(input('Teve contato com alguém com suspeita ou que foi confirmado? 1-SIM  2-NÃO '))
febre = int(input('Está com febre? 1-SIM     2-NÃO '))
ar = int(input('está com falta de ar? 1-SIM   2-NÃO '))
tosse = int(input('está tossindo (tosse seca)  1-SIM   2-NÃ0 '))
corisa = int(input('Seu nariz está com corisa ou está com catarro? 1-SIM   2-NÃO '))
if contato == 1 and febre == 1 and ar == 1 and tosse == 1 and corisa == 2:
    print('todos os sintomas apontam que você está com Corona Vírus')
elif contato == 1 or febre == 1 or ar == 1 or tosse == 1 or corisa == 2:
    print('não há certeza que você está com corona virus')
elif contato == 2 and febre == 2 and ar == 2 and tosse == 2 and corisa == 1:
    print('fique tranquilo! Você não tem os sintomas.')
'''#exibe a parte inteira de um numero ex. parte inteira de 6.127 é 6
from math import trunc
num = float(input('digite um numero: '))
print('o valor digitado foi {} e a sua parte inteira é {}'.format(num, trunc(num))) ou sem importar'''

num = float(input('digite um numero: '))
print('o numero digitado é {} e sua parte inteira é {}'.format(num, int(num)))
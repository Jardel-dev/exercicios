n1 = int(input('um valor: '))
n2 = int(input('outro valor: '))
s = n1 + n2
div = n1 / n2
multi = n1 * n2
divint = n1 // n2
resto = n1 % n2
exp = n1 ** n2
print('a soma vale: {:.2f}, a divisão {:.2}, a multiplicação vale {}'.format(s, div,multi),end='')
print('o resto da divisão é {} e a potencia é {}'.format(resto,exp))

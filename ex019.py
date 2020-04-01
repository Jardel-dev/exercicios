#sorteia um nome de uma lista
import random
pessoa1 = str(input('nome: '))
pessoa2 = str(input('nome: '))
pessoa3 = str(input('nome: '))
pessoa4 = str(input('nome: '))
lista = [pessoa1, pessoa2, pessoa3, pessoa4]
escolhido = random.choice(lista)
print('o escolhido foi {}'.format(escolhido))

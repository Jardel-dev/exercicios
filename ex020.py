#altera a ordem dos nomes
from random import shuffle
nome1 = str(input('nome: '))
nome2 = str(input('nome: '))
nome3 = str(input('nome: '))
nome4 = str(input('nome: '))
lista = [nome1, nome2, nome3, nome4]
shuffle(lista)
print('a ordem de apresentação é: ')
print(lista)
#analisa string
nome = str(input('digite um nome: ')).upper().strip()
print('a letra A aparece {}'.format(nome.count('A'), 'veze(s)'))
print('primeira letra A está na posição: {}'.format(nome.find('A')+1))
print('a ultima letra A aparece na posição: {}'.format(nome.rfind('A')+1))

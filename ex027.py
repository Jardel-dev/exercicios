#consulta primeiro e ultimo nome da pessoa
n = str(input('digite seu nome completo: '))
nome = n.split()
print('o primeiro nome é {}'.format(nome[0]))
print('seu último nome é {}'.format(nome[len(nome)-1]))
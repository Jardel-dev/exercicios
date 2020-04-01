# analisa frases
nome = (input('digite seu nome e irei analisar '))
print(nome[0:30])
print('Seu nome com letras maiúsculas fica assim: ',nome.upper())
print('em minuscúlas fica assim: ', nome.lower())
print(' o nome {} possui: '.format(nome), len(nome),'letras e espaços')
print('o primeiro nome tem', len(nome))
separa = nome.split()
print('seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
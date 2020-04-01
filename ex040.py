#media das notas do aluno
n1 = float(input('nota 1: '))
n2 = float(input('nota 2: '))
media = (n1 + n2) / 2
if media < 5.0:
    print('REPROVADO')
elif media > 7.0:
    print('APROVADO')
else:
    print('RECUPERAÇÃO')
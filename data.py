from datetime import date

data_atual = date.today()
print(f'{data_atual.year}')
print('digite a data de nascimento')
ano = int(input('ano '))
a = data_atual.year - ano
print(f'{a}')

#ler o ano de nasc de 7 pessoas e dizer qtas atingiram a maior idade e qtas ainda não atingiram a maior idade
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pessoa in range(1, 4):
    nasc = int(input(f'Em que ano a {pessoa}ª pessoa nasceu? '))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
        print('Essa pessoa é maior')
    else:
        totmenor += 1
        print('Essa pessoa é menor')
    print(f'o total de pessoas maiores é {totmaior} e de pessoas menores é {totmenor}')
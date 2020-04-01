#alistamento militar
from datetime import date
data = date.today().year
sexo = int(input('digite   1 - FEMININO   2 - MASCULINO\n'))
if sexo == 2:
    print('todo homem precisa se apresentar ao serviço militar')
    idade = int(input('qual sua idade? '))
    if idade <= 17:
        print('você ainda não tem idade para se apresentar')
    elif idade > 21:
        print('você ja passou do prazo para se alistar, procure uma junta militar proximo da sua casa, tá ok? ')
    elif idade >= 18 and idade <= 19:
        print(' você está lascado! vai ter que beber sangue de galinha no quartel, sentir frio e fome no treinamento')
else:
    print('você não tem obrigação de se alistar por ser mulher')
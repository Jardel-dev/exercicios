#aumento de salário
salario = float(input('digite um salário '))
if(salario >= 1250):
    print('o salário acima de 1.250 terá um aumento de 10% passando para R${:.2f}'.format((salario*10)/100+salario))
else:
    print('o salario abaixo de 1.250 terá um aumento de 15% passando para {:.2f}'.format((salario*15)/100+salario))
#aumento salarial
salario = float(input('valor do salario: R$'))
perc = int(input('digite o percentual de aumento: '))
aumento = (salario*perc)/100
print('o salario R${:.2f} terá um aumento de {}% sendo o salario atualizado para: R${:.2f}'.format(salario,perc,salario+aumento))
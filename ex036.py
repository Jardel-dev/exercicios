#aprovar emprestimo bancário ---- travei nesse
print('o valor da parcela não pode exceder 30% do salário')
casa = float(input('valor da casa: R$'))
salario = float(input('salario do comprador: R$'))
anos = int(input('duração do financiamento: '))
prestacao = casa/(anos * 12)
minimo = salario * 30 / 100
print(f'para pagar uma casa de R${casa:.2f} em {anos} anos', end='')
print(f' a prestação será de R${prestacao:.2f}')
if prestacao <= minimo:
    print(' emprestimo CONCEDIDO')
else:
    print('emprestimo NEGADO')
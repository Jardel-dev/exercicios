#calculo de porcentagem de desconto
prod = float(input('valor do produto: R$'))
porc = int(input('% do desconto: '))
desc = (prod*porc)/100
print('o desconto é de R${:.2f} o produto com desconto será R${:.2f} '.format(desc, prod-desc))

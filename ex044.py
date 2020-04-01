#calcule pruduto preço normal e condição de pagamento
vlprod = float(input('valor do produto sem acrescimo: '))
condpgto = str(input('condição de pagamento: \n1-DINHEIRO ou CHEQUE\n2-CARTÃO\n3-2X CARTÃO\n4-3X OU MAIS NO CARTÃO\n'))

if condpgto == '1':
    print(f'Na condição de 1-DINHEIRO ou CHEQUE o desconto é de 10% {vlprod-(vlprod*10/100):.2f}')
elif condpgto == '2':
    print(f'Valor à vista no cartão: 5% de desconto R${vlprod-(vlprod*5/100):.2f}')
elif condpgto == '3':
    print(f'parcelado em 2x o valor não tem desconto')
else:
    parcelas = int(input('quantas parcelas? '))
    total = vlprod + (vlprod*20/100)

    print(f'acima de 3x, acrescimo de 20%: valor do produto R${vlprod:.2f} + valor do acrescimo: R${(vlprod*20/100):.2f}')
    print(f'Valor da parcela: R${total/parcelas:.2f}')
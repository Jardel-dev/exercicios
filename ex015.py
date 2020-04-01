#aluguel de carro
dias = int(input('quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
base = (dias*60)+(km*0.15)
print('Total a pagar pelos dias de uso: R${:.2f}\n total a pagar pelos km rodados R${:.2f}\n total R${:.2f}'.format(dias*60,km*0.15, base))
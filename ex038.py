#compara dois numeros e informa qual é o maior
n1 = int(input('primeiro numero '))
n2 = int(input('segundo numero '))
if n1 > n2:
    print('o PRIMEIRO número é maior que o segundo')
elif n2 > n1:
    print('o SEGUNDO número é maior que o primeiro')
else:
    print('os dois números são iguais')
#calcular a soma entre todos os numeros impares que são multiplos de três e que se encontram no intervalo de 1 ate 500
soma = 0
contador = 0
for c in range(1, 501,2):
    if c % 3 ==0:
        contador = contador + 1
        soma = soma + c
print(f'Temos {contador} numeros impares multiplos de três e a soma de todos os é {soma}')

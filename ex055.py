#programa que leia o peso de cinco pessoas e mostre quem é o mais e o menos pesado
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f'digite o peso da {p}ª pessoa '))
    if p == 1:
        maior == peso
        menor == peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior}')
print(f'o menor peso lido foi de {menor}')


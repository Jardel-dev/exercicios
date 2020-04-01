#leia seis numeros inteiros e mostre a soma de apenas aqueles que forem pares
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input(f'digite 0 {c}º valor: '))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print(f'foi informado {cont} numeros e a soma deles é {soma}')
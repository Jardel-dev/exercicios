#ler um numero inteiro e informar se ele é primo ou não
num = int(input('digite um numero para saber se é ou não primo: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(f'{c} ', end='')
print(f'\no numero {num} foi divisivel {tot} vezes')
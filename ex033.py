#ler 3 numeros e dizer qual é o maior
num1 = int(input('digite um numero '))
num2 = int(input('digite um numero '))
num3 = int(input('digite um numero '))
#verifica quem é o menor
menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3

#verifica quem é o maior
maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3
print('o menor dos numeros é {}'.format(menor))
print('o maior dos numeros é {}'.format(maior))

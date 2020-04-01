#ler o primeiro termo e a razão de uma PA. no final mostre os 10 primeiros termos da progressão.
primeiro = int(input('primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print(f'{c}', end=' -> ')
print('ACABOU')
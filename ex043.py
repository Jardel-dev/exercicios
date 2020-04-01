#analise de peso
peso = float(input('digite seu peso: '))
altura = float(input('digite sua altura: '))
imc = peso / (altura * 2)
if imc < 18.5:
    print(f' seu IMC é {imc:.2f} abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print(f'seu IMC é {imc:.2f} peso ideal')
elif imc >= 25 and imc < 30:
    print(f'seu IMC é {imc:.2f} sobrepeso')
elif imc >= 30 and imc < 40:
    print(f'seu IMC é {imc:.2f} obeso')
else:
    print(f'seu IMC é {imc:.2f} obesidade morbida')
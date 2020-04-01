#tabuada utilizando o for, usuário digita um numero e é exibida a tabuada deste numero
num = int(input('digite um número para a tabuada: '))
for c in range(0, 11):
    print(c, '  x ', num, ' = ',num * c)
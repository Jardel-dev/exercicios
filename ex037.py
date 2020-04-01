# conversor de bases
print('digite uma das bases para conversão')
print('1 - BINARIO\n2 - OCTAL\n3 - HEXADECIMAL')
num = int(input('digite um numero inteiro: '))
opcao = int(input('sua opção: '))
if opcao == 1:
    print(f'A base em bináro é {bin(num)[2:]}')
elif opcao == 2:
    print(f'A base em OCTAL é {oct(num)[2:0]}')
elif opcao == 3:
    print(f'A base em HEXADECIMAL é: {hex(num)[2:]}')
else:
    print('opção inválida')
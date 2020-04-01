#analisando triangulo
ld1 = int(input('digite o primeiro lado do triangulo'))
ld2 = int(input('digite o segundo  lado do triangulo'))
ld3 = int(input('digite o terceiro lado do triangulo'))
if ld1 < ld2 + ld3 and ld2 < ld1 + ld3 and ld3 < ld1 + ld2:
    print('essas medidas formam um triangulo', end='')
    if ld1 != ld2 != ld3 != ld1:
        print(' ESCALENO')
    elif ld1 == ld2 == ld3:
        print(' EQUILATERO')
    else:
        print(' ISOSCELES')
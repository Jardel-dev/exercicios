#após digitar o angulo informa o seno o cosseno a a tangente
from math import sin, cos, tan, radians
ang = float(input('digite o valor do angulo: '))
print('o angulo de {:.2f} possui o seno de {:.2f}\no angulo de {:.2f} o cosseno é {:.2f}\no angulo de {:.2f} a tangente é {:.2f}'.format(ang, sin(radians(ang)), ang, cos(radians(ang)), ang, tan(radians(ang))))
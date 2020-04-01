#catetos e hipotenuza
from math import hypot
co = float(input('comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjascente: '))
print('com o cateto oposto de {} e cateto adjascente de {} a hipotenuza é {:.2f}'.format(co, ca, hypot(co,ca)))

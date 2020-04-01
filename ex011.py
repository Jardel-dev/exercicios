#parede
largura = float(input('largura da parede: '))
altura = float(input('altura da parede: '))
area = largura * altura
print('a parede de {}m de largura e {}m de altura possui {}m²'.format(largura,altura,area))
print('será necessário {}lts de tinta'.format(area/2))
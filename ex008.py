#informa a conversão de medidas
mt = float(input('digite uma medida que será exibida em metros: '))
km = mt / 1000
hm = mt / 100
dam = mt / 10
dm = mt * 10
cm = mt * 100
mm = mt * 1000
print('{} metros tem \n {} km \n {} hectometros \n {} decametros \n {} centimetros e \n {} milimetros'.format(mt,km,hm,dam,dm,cm,mm))
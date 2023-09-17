d = float(input('Uma distancia em metros: '))
km = d / 1000
hm = d / 100
dam = d / 10
dm = int(d * 10)
cm = int(d * 100)
mm = int(d * 1000)
print('A medida de {} corresponde a \n{}km \n{}hm \n{}dam'.format(d, km, hm, dam))
print('{}dm \n{}cm \n{}mm'.format(dm, cm, mm))
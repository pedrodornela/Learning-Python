l1 = float(input('Primeiro segmento: '))
l2 = float(input('Segundo segmento: '))
l3 = float(input('Terceiro segmento: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Com os valores {} {} e {} é possível formar um triângulo!!'.format(l1, l2, l3))
else:
    print('Com os valores {}  {} e {} não é possível formar um triângulo.'.format(l1, l2, l3))

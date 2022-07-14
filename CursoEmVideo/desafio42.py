l1 = int(input('Primeiro segmento: '))
l2 = int(input('Segundo segmento: '))
l3 = int(input('Terceiro segmento: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('É possível formar um triângulo com os valores {}, {}, {}'.format(l1, l2, l3))
    if l1 == l2 == l3:
        print('Esse triângulo é EQUILÁTERO')
    elif l1 != l2 != l3:
        print('Esse triângulo é ESCALENO')
    else:
        print('Esse triângulo é ISÓSCELES')
else:
    print('Não é possível formar um triângulo com os valores {}, {}, {}'.format(l1, l2, l3))

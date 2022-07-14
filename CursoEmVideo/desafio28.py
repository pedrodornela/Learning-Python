import random
maq = random.randint(0, 5)
usuario = int(input('Qual número entre 0 e 5 máquina escolheu?: '))

if maq == usuario:
    print('Você venceu!!')
else:
    print('Você perdeu!!')
print('Número que a máquina escolheu {}'.format(maq))
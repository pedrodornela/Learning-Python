import random
maq = random.randint(0, 2)

usuario = int(input('''Suas opções: 
[0] PEDRA
[1] PAPEL
[2] TESOURA
Qual a sua jogada? '''))

if maq == 0 and usuario == 0 or maq == 1 and usuario == 1 or maq == 2 and usuario == 2:
    print('EMPATE')
elif maq == 0 and usuario == 1:
    print('Você venceu!')
elif maq == 0 and usuario == 2:
    print('A máquina venceu!')
elif maq == 1 and usuario == 0:
    print('A máquina venceu!')
elif maq == 1 and usuario == 2:
    print('Você venceu!')
elif maq == 2 and usuario == 0:
    print('Você venceu!')
elif maq == 2 and usuario == 1:
    print('A máquina venceu!')
else:
    print('DIGITE UM VALOR VÁLIDO!!!')

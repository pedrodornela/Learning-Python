veloc = int(input('Qual a velocidade do carro?: '))

if veloc > 80:
    multa = (veloc % 80) * 7
    print('VOCÊ FOI MULTADO!! O valor da multa é de R${}'.format(multa))

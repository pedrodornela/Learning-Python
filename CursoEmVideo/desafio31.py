rodado = int(input('Qual a distância da viagem em quilometros: '))

if rodado <= 200:
    v1 = rodado * 0.5
    print('O valor da passagem é de R${}'.format(v1))
else:
    v2 = rodado * 0.45
    print('O valor da passagem é de R${}'.format(v2))
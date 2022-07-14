dia = int(input('Por quantos dias o carro foi alugado?: '))
km = float(input('Quantos quilômetros o carro alugado rodou?: '))
dt = dia * 60
kt = km * 0.15
t = dt + kt
print('O preço apagar pelo carro alugado por dias rodados e quilometragem é de {}{:.2f}{}'.format('\033[0;32m', t, '\033[m'))
n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n**(1/2)
print('Lido o número {}, seu dobro é {}, seu triplo é {} e sua raiz quadrada é {}{:.2f}{}'.format(n, d, t, '\033[7;30m', r, '\033[m'))
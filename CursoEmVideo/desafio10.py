r = int(input('Quantos reais você possui?? '))
u = r / 5.35
print('Você pode comprar com R${}{}{} -> US${}{:.2f}{}'.format('\033[4;32m', r, '\033[m', '\033[4;31m', u, '\033[m'))

s = float(input('Salário do funcionário: R$'))
print('O novo salário do funcionário é R${}{:.2f}{}'.format('\033[0;36m', s * 1.15, '\033[m'))

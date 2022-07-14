salario = int(input('Digite o seu salário: '))

if salario <= 1250:
    inf = salario + (salario * 0.15)
    print('Seu novo salário é de R${}'.format(inf))
else:
    sup = salario + (salario * 0.1)
    print('Seu novo salário é de R${}'.format(sup))

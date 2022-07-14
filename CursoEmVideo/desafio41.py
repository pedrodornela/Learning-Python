idade = int(input('Digite sua idade, para saber a categoria: '))

if idade <= 9:
    print('Sua categoria é MIRIM')
elif idade <= 14:
    print('Sua categoria é INFANTIL')
elif idade <= 19:
    print('Sua categoria é JUNIOR')
elif idade == 20:
    print('Sua categoria é SÊNIOR')
else:
    print('Sua categoria é MASTER')

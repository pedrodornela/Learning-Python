ano = int(input('Digite um ano: '))

if ano % 400 == 0 or ano % 4 == 0 and ano != (ano % 100 == 0):
    print('O ano {} é bissexto!!'.format(ano))
else:
    print('O ano {} não é bissexto!!'.format(ano))

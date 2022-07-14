n = -1
termo = int(input('Digite um valor: '))
razao = int(input('Digite o valor da razão: '))
#PA = termo + (termo - 1) * razao
print('Os 10 primeiros valores da PA são:')
for c in range(0, 10, 1):
    PA = termo + (n + 1) * razao
    n += 1
    print(PA)

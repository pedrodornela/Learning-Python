num = int(input('Digite um número: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[36m', end='')
        total += 1
    else:
        print('\033[m', end='')
    print('{} '.format(c), end='')
if total > 2 or total == 1:
    print('\n\033[mO número {} não é primo!'.format(num))
else:
    print('\n\033[mO número {} é primo'.format(num))
print('\n\033[mO número {} foi dividido {} vezes!'.format(num, total))

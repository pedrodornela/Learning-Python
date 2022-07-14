n = int(input('Digite um número: '))
s = n + 1
a = n - 1

print('Analisado o valor {}{}{}, seu antecessor é {}{}{} e o seu sucessor é {}{}{}'.format('\033[1;33m', n, '\033[m', '\033[1;31m', a, '\033[m', '\033[1;34m', s, '\033[m'))

n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
nome = input('Qual é o seu nome?? ')
print('Prazer {:=^10}!'.format(nome) )

s = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2
divint = n1 // n2
rest = n1 % n2
pot = n1 ** n2

print('A soma, subtração, multiplicação, divisão, divisão inteira, resto e potencia entre {} e {} é: \n {}, {}, {}, {:.3f}, {}, {}, {}'.format(n1, n2, s, sub, mult, div, divint, rest, pot))

#  \n -> quebra linha
#  :.3f -> casas decimais depois da vírgula

print('ola' * 5)
print('='*15)


soma = 0
for c in range(1, 501):
    if c % 2 == 1 and c % 3 == 0:
        soma += c
        #print(c)
print('A soma do intervalo 1 até 500, de números ímpares e múltiplos de 3 é: {}'.format(soma))

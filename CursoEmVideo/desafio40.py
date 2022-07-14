v1 = float(input('Valor da primeira nota: '))
v2 = float(input('Valor da segunda nota: '))
media = (v1 + v2) / 2
print('O valor da sua média foi {:.1f}'.format(media))
if media >= 7.0:
    print('Aprovado!')
elif media < 5.0:
    print('Reprovado!')
else:
    print('Recuperação!')

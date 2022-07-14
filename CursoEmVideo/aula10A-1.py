nome = str(input('Qual o seu nome?: '))
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2

print('A média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Boa média {}'.format(nome))
else:
    print('Estude mais {}'.format(nome))

#OU
#forma simplificada
print('Parabéns {}'.format(nome) if m >= 6.0 else 'Estude mais {}'.format(nome))
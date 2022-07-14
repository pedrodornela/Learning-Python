ano_nasc = int(input('Qual o ano do seu nascimento: '))

from datetime import date
atual = date.today().year

idade = atual - ano_nasc

print('Ano de nascimento: {}'.format(ano_nasc))
print('Quem nasceu em {} tem {} ano(s) em {}'.format(ano_nasc, idade, atual))
if idade < 18:
    saldo = 18 - idade
    a = atual + saldo
    print('Faltam {} anos para o alistamento!'.format(saldo))
    print('Seu alistamento será em {}'.format(a))
elif idade == 18:
    print('Você precisa se alistar ao exército esse ano IMEDIATAMENTE, {}!'.format(atual))
else:
    saldo = idade - 18
    a = atual - saldo
    print('Já passou a época de se alistar ao exército, foi há {} ano(s) átras!'.format(saldo))
    print('Seu alistamento foi em {}'.format(a))

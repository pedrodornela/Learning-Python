maior = 0
menor = 0
for c in range(0, 7, 1):
    data = int(input('Qual a sua data de nascimento? '))
    from datetime import date
    atual = date.today().year
    idade = atual - data
    if idade < 18:
        menor += 1
    else:
        maior += 1

print('Possuem {} maiores de idade e {} menores de idade.'.format(maior, menor))

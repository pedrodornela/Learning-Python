a = int(input('Digite o 1° número: '))
b = int(input('Digite o 2° número: '))
c = int(input('Digite o 3° número: '))
#Verificar menor valor
menor = a

if b < a and b < c:
    menor = b

if c < a and c < b:
    menor = c
#Verificar maior valor
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}{}{}'.format('\033[1;34m', menor, '\033[m'))
print('O maior valor digitado foi {}{}{}'.format('\033[1;31m', maior, '\033[m'))

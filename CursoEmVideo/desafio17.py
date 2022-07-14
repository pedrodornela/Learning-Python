import math
num1 = int(input('Digite o valor do cateto oposto: '))
num2 = int(input('Digite o valor do cateto adjacente: '))

ipote = math.hypot(num1, num2)
print('O comprimento da ipotenusa vale: {:.2f}'.format(ipote))
l = int(input('Qual a largura da parede? '))
a = int(input('Qual a altura da parede? '))
ar = (a * l)
li = ar / 2
print('Será necessário {}{}{} Litros de tinta, para cobrir {}{}{} metros quadrados'.format('\033[0;34m', li, '\033[m', '\033[0;33m', ar, '\033[m'))

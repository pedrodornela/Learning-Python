nome = str(input('Qual o seu nome?? '))

if nome == 'Pedro':
    print('Que nome bonito!')
elif nome == 'Tiago' or nome == 'Alysson' or nome == 'Fernando':
    print('O cara foda!')
elif nome == 'Eduardo':
    print('Bom dia chefe!')

print('Tenha um bom dia, {}!'.format(nome))

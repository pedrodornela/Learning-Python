n = input('Digite algo a ser verificado: ')

print('O valor está em letra maiuscula??:', '\033[1;30;41m', n.isupper(), '\033[m')
print('O valor é númerico??: ', '\033[4;30;42m', n.isnumeric(), '\033[m')
print('O valor é alphnumerico??: ', '\033[7;32;47m', n.isalnum(), '\033[m')
print('O valor é alfabetico??: ', '\033[0;33;45m', n.isalpha(), '\033[m')

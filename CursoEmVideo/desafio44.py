valor = int(input('Digite o valor do produto: '))
forma = int(input('''Digite a forma de pagamento:
                     DIGITE 0 PARA: DINHEIRO/CHEQUE
                     DIGITE 1 PARA: À VISTA NO CARTÃO
                     DIGITE 2 PARA: ATÉ 2X NO CARTÃO
                     DIGITE 3 PARA: 3X NO CARTÃO OU MAIS: '''))

if forma == 0:
    pagar = valor - (valor * 0.1)
    print('O valor a pagar é de R${}'.format(pagar))
elif forma == 1:
    pagar = valor - (valor * 0.05)
    print('O valor a pagar é de R${}'.format(pagar))
elif forma == 2:
    print('O valor a pagar é de R${}'.format(valor))
elif forma == 0:
    pagar = valor + (valor * 0.2)
    print('O valor a pagar é de R${}'.format(pagar))
else:
    print('DIGITE UMA FORMA DE PAGAMENTO VÁLIDA!!!')

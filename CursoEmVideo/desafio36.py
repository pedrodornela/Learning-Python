casa = int(input('Qual o valor da casa?: '))
sala = float(input('Qual o seu salário?: '))
ano = int(input('Em quantos anos será pagoo emprestimo?: '))

prestacao = casa / (ano * 12)

if prestacao > (sala * 0.3):
    print('O empréstimo não podera ser realizado!')
else:
    print('O empréstimo podera ser realizado!')

#print(prestacao)
#print((sala * 0.3))

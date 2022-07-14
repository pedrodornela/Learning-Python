peso = int(input('Digite seu peso: '))
altura = int(input('Digite sua altura em centímetros: '))
altura1 = altura/100

imc = peso / (altura1 ** 2)
print('Seu índice de massa corporal é igual a: {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif imc <= 24.9:
    print('Peso ideal')
elif imc <= 29.9:
    print('Sobrepeso')
elif imc <= 39.9:
    print('Obesidade')
else:
    print('Obesidade mórbida')
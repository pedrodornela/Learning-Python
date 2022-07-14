tp = float(input('Informe a temperatura em °C: '))
f = (tp * (9/5)) + 35
print('A temperatura de {}{}{}°C corresponde a {}{}{}°F'.format('\033[0;33m', tp, '\033[m', '\033[0;31m', f, '\033[m'))
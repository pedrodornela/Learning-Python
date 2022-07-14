import math
ang = int(input('Digite um ângulo qualquer: '))
rad = math.radians(ang)
s = math.sin(rad)
c = math.cos(rad)
t = math.tan(rad)
print('O valor de seu seno é {:.3f} do cosseno é {:.3f} e da tangente é {:.3f} '.format(s, c, t))

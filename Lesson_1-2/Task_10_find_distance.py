# Найти расстояние между двумя точками пространства.



import math


Xa = int(input('x1: '))
Xb = int(input('x2: '))

Ya = int(input('y1: '))
Yb = int(input('y2: '))

Za = int(input('z1: '))
Zb = int(input('z2: '))


print(math.sqrt((Xa - Xb)**2 + (Ya - Yb)**2 + (Za - Zb)**2))


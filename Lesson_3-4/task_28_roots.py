# Найти корни квадратного уравнения Ax² + Bx + C = 0
# a. Математикой
# b. Используя дополнительные библиотеки*
import math

a = 2
b = 4
c = 7

discr = b ** 2 - 4 * a * c
print(discr)

if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print(x1, x2)
elif discr == 0:
    x = -b / (2 * a)
    print(x)
else:
    print('No')
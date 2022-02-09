# Указав номер четверти прямоугольной системы координат, показать допустимые значения координат для точек этой четверти.

number = int(input())


if number == 1:
    print('X = from 0 to ∞; Y = from 0 to ∞')
if number == 2:
    print('X = from 0 to -∞; Y = from 0 to ∞')
if number == 3:
    print('X = from 0 to -∞; Y = from 0 to -∞')
if number == 4:
    print('X = from 0 to ∞; Y = from 0 to -∞')
else:
    print('Incorrect')
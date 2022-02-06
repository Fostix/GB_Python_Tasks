# Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У 


x = int(input('Enter coordinate x: '))
y = int(input('Enter coordinate y: '))

if x > 0 and y > 0:
    print('Первая плоскость')
elif x < 0 and y > 0:
    print('Вторая плоскость')
elif x < 0 and y < 0:
    print('Третья плоскость')
elif x > 0 and y < 0:
    print('Четвёртая плоскость')
elif x == 0 and y !=0:
    print('asix y')
elif y == 0 and x !=0:
    print('asix x')
else:
    print('Лежит на оси x и y')

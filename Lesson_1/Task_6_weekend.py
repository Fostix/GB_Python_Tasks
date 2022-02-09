# Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.

list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
day = int(input('Enter day: '))
day -= 1

if day > 6 or day < 0:
    print('Incorrect')
elif day == 5 or day == 6:
    print('Weekend', list[day])
else:
    print('Work', list[day])




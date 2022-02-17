# Найти сумму чисел списка стоящих на нечетной позиции.

import random

here_numbers = []
length_list = int(input('Enter list length: '))
sum = 0

for i in range(length_list):
    here_numbers.append(random.randrange(10))

for i in range(1, length_list,2):
        sum += here_numbers[i]



print(here_numbers)
print(sum)



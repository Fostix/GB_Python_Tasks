# Найти произведение пар чисел в списке. 
# Парой считаем первый и последний элемент, 
# второй и предпоследний и т.д. 
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]

from itertools import product
from fill_list import fill_method as fill

numbers_length = int(input('Enter list length: '))
numbers = []
fill(numbers, numbers_length)
products = []
# print(round((len(numbers) + 1) / 2))

for i in range(((len(numbers)) + 1) // 2):
    products.append(numbers[i] * numbers[-1 - i])


print(numbers)
print(products)
# Задать список из N элементов, заполненных числами из [-N, N].
# Найти произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.


from random import randrange


here_numbers = []
length = int(input('Enter length: '))

for i in range(length):
    here_numbers.append(randrange(-length, length))

print(here_numbers)

product_num = 1
file_here = r'D:\GitHub\Python practic\GB_Tasks\Lesson_2\files\text.txt'
file_temp = open(file_here, 'r')
for search in file_temp:
    int_search = int(search)
    test_lenth = (len(here_numbers) - 1)
    if int_search >= test_lenth:
        continue
    product_num *= here_numbers[int_search]


print(product_num)

file_temp.close()
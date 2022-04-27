# Дан список чисел. Создать список в который попадают числа, описывающие
# возрастающую последовательность и содержащие максимальное количество
# элементов.
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
# [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]
# Порядок элементов менять нельзя

from Task_36 import func as f


numbers = [1, 5, 2, 3, 4, 6, 1, 7]
test2 = [5, 2, 3, 4, 6, 1, 7]
test3 = [5, 4, 3, 2, 1]
test4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
test5 = [9, 1, 7, 2, 5, 1, 3]




def f_2(numbers, index):

    new_list = [numbers[index]]
    min_num = new_list[0] + 1
    index += 1
    while min_num - 1 != max(numbers):
        i = index
        while i < len(numbers):
            if min_num == numbers[i]:
                new_list.append(numbers[i])
                min_num += 1
                index = i + 1
                break
            i += 1
        else:
            min_num += 1

    return new_list





def func(numbers):
    max = f(numbers, 0)
    for i in range(len(numbers)):
        list_1 = f(numbers, i)
        list_2 = f_2(numbers, i)
        if len(list_2) > len(max):
            max.clear()
            max = list_2
        elif len(list_1) > len(max):
            max.clear()
            max = list_1

    return max





print(func(test5))
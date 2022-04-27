# Дан список чисел. Создать список, в который попадают числа, описываемые
# возрастающую последовательность. Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7]
# или [1, 6, 7] и т.д. Порядок элементов менять нельзя


numbers = [1, 5, 2, 3, 4, 6, 1, 7]


def func(numbers, index):
    new_numbers = [numbers[index]]
    i = index + 1
    while i < len(numbers):
        if numbers[i] > max(new_numbers):
            new_numbers.append(numbers[i])
        i += 1
    return new_numbers


# print(func(numbers, 0))



# Строка содержит набор чисел. Показать большее и меньшее число
# Символ-разделитель - пробел


def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)


text = '18 6 33 5 7 89 9 3 4 56 8 0 44 23 2'
numbers = [i for i in text.split()]
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

g = quicksort(numbers)
print(g)

print(f'{g[0]} min')
print(f'{g[-1]} max')


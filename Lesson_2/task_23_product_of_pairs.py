from fill_list import fill_method as fill

numbers_length = int(input('Enter list length: '))
numbers = []
fill(numbers, numbers_length)

# print(round((len(numbers) + 1) / 2))

for i in range(((len(numbers)) + 1) // 2):
    print(numbers[i] * numbers[-1 - i])


print(numbers)
# Сформировать список из N членов последовательности.
# для N = 5: 1, -3, 9, -27, 81 и т.д
list = []
length = int(input('Enter length list: '))
three = 3
number = 1

for i in range(length):
        list.append(number)
        number *= -three


print(list)

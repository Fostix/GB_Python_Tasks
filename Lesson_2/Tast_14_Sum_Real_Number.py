# Подсчитать сумму цифр в вещественном числе.

import string


number = 5.34056
sum = 0

number = str(number)
for i in number:
    if i != '.':
        sum += int(i)



print(sum)

# for i in range(5):
#     number = number * 10


# print(number)


# for i in range(5):
#     sum += int(number % 10)
#     number = number / 10

# print(sum)
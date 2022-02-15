# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]



numbers = []
startNum = 2
ham = 1

for i in range(9):
    numbers.append(numbers[i] * startNum)
    startNum +=1

print(numbers)


# for i in range(9):
#     sum = sum * startNum
#     numbers.append(sum)
#     startNum +=1

# print(numbers)
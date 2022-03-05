# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]



numbers = [1]
startNum = 2

for i in range(9):
    numbers.append(numbers[i] * startNum)
    startNum +=1

print(numbers)


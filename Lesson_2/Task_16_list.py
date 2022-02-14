# Задать список из n чисел последовательности (1+1/n)n и вывести на экран их сумму


from unittest import result


length = 6
mrList = []
sum = 0


for i in range(1, length + 1):
    length = (1 + 1 / i) ** i
    mrList.append(length)
    sum += length



print(mrList)
print(sum)
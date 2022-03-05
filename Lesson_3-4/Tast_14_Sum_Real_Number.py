# Подсчитать сумму цифр в вещественном числе.

number = 5.34056
sum = 0

for i in range(6):
    number = number * 10


for i in range(6):
    sum += int(number % 10)
    number = number / 10

print(sum)
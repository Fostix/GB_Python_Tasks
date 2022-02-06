# Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30.

from audioop import mul


number = int(input('Enter number: '))
multiplicity = 5

for i in range(4):
    if number % multiplicity == 0:
        print

    print(multiplicity)
    if multiplicity < 15:
        multiplicity += 5
    else:
        multiplicity *= 2









# Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30.


number = int(input('Enter number: '))
multiplicity = 30
result = 0

for i in range(4):
    if multiplicity == 30:
        if number % multiplicity == 0:
            break
        multiplicity /= 2
    else:
        if number % multiplicity == 0:
            result += 1
        multiplicity -= 5


if result == 2:
    print('good')
else:
    print('bad')

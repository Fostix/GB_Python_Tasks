# По двум заданным числам проверить является ли одно квадратом второго.

first_number = int(input('Enter number a: '))
second_number = int(input('Enter number b: '))
result = first_number

if first_number > second_number:
    result = second_number

result **= 2
if result == first_number:
    print(f'{first_number} is the square {second_number}')
elif result == second_number:
    print(f'{second_number} is the square {first_number}')
else:
    print('No number is the square of another')
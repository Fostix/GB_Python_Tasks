# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k. 
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random


# with open(r'D:\GitHub\Python practic\GB_Tasks\Lesson_5-6\files\text.txt', 'r') as g:
#     for i in range(1,100):
#         for i in range(1,100):
#             g.write(f'{i} ')




def poly(k):
    coeffs = [random.randint(0,5) for x in range(k+1)]
    print(coeffs)
    th = []
    a_zero = [f'{coeff} * 1' for num, coeff in enumerate(coeffs) if coeff != 0 if num > k - 1]
    a_one = [f'{coeff}x' for num, coeff in enumerate(coeffs) if coeff != 0 if num == k - 1]
    a = [f'{coeff}x^{k - num}' for num, coeff in enumerate(coeffs) if coeff != 0 if num < k - 1]

    th.append(a)
    th.append(a_one)
    th.append(a_zero)



    return th







g = poly(9)
print(len(g))
print(g)
for i in g:
    print(i)
# data = open('file2.txt', 'a')
# for i in range(1, len(g)):
#     data.write(f' + {g}')


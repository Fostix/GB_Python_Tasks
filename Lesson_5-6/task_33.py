# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k. 
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random


file = open(r'D:\GitHub\Python practic\GB_Tasks\Leesson_3\files\text.txt', 'w')
for i in range(101):
    file.write(f'{i} ')


# file = [random.randint(0, 101) for i in range(3)]



# def poly(k):
#     coeffs = [random.randint(0,5) for x in range(k+1)]
#     print(coeffs)
#     a = [f'{coeff}x^{k - num}' for num, coeff in enumerate(coeffs) if coeff != 0 or coeff != 1]
#     return ' + '.join(a)


# print(poly(5))
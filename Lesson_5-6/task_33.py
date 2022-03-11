# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k. 
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random as r


def poly(k):
    coeffs = [r.randint(0,5) for x in range(k+1)]
    a = [f'{coeff}x^{k - num}' for num, coeff in enumerate(coeffs) if coeff != 0 if num < k - 1] + [f'{coeff}x' for num, coeff in enumerate(coeffs) if coeff != 0 if num == k - 1] + [f'{coeff}' for num, coeff in enumerate(coeffs) if coeff != 0 if num > k - 1]
    return ' + '.join(a)

def writer_file(what):
    with open(r'D:\GitHub\Python practic\GB_Tasks\Lesson_5-6\files\task33.txt', 'a') as mr_writer:
        mr_writer.write(f'{g} = 0\n')



g = poly(34)
print(f'{g} = 0')
writer_file(g)
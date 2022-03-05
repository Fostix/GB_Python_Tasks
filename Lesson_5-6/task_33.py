# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k. 
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random


# with open(r'D:\GitHub\Python practic\GB_Tasks\Lesson_5-6\files\text.txt', 'r') as g:
#     for i in range(1,100):
#         for i in range(1,100):
#             g.write(f'{i} ')




# def poly(k):
#     coeffs = [random.randint(0,5) for x in range(k+1)]
#     print(coeffs)
#     th = []
#     a_zero = [f'{coeff} * 1' for num, coeff in enumerate(coeffs) if coeff != 0 if num > k - 1]
#     a_one = [f'{coeff}x' for num, coeff in enumerate(coeffs) if coeff != 0 if num == k - 1]
#     a = [f'{coeff}x^{k - num}' for num, coeff in enumerate(coeffs) if coeff != 0 if num < k - 1]
#     a_one = str(a_one)
#     print(type(a_one))
#     th.append(' + '.join(a))
#     th.append((a_one))
#     th.append((a_zero))

#     #b = [f'{coeff}X^{k - num}' for num, coeff in enumerate(coeffs) if coeff != 0 if num == 1]
#     th = str(th)
#     print(type(th))
#     th = th.replace(',', ' +')
#     th = th.replace('[', '')
#     th = th.replace(']', '')
#     ##print(th)
#     return th



def poly(k):
    coeffs = [random.randint(0,5) for x in range(k+1)]
    print(coeffs)
    th = []
    a_zero = [f'{coeff} * 1' for num, coeff in enumerate(coeffs) if coeff != 0 if num > k - 1]
    a_one = [f'{coeff}x' for num, coeff in enumerate(coeffs) if coeff != 0 if num == k - 1]
    a = [f'{coeff}x^{k - num}' for num, coeff in enumerate(coeffs) if coeff != 0 if num < k - 1]
    print(type(a))
    a = str(a)
    a_one = str(a_one)
    a_zero = str(a_zero)

    a.join(a_one)
    a.join(a_zero)
    print(type(a))

    th = (f'{a} {a_one} {a_zero}')
    th = ' + '.join()
    print(th)
    return th


# def mr_write(a):
#     print(str(a))
#     data = open(r'D:\GitHub\Python practic\GB_Tasks\Lesson_5-6\files\text.txt', 'r')
    
#     data.writelines(a)
#     data.close()






# def comb(a):
#     g = poly(a)
#     print(g)




g = poly(9)
print(g)



# with open(r'D:\GitHub\Python practic\GB_Tasks\Lesson_5-6\files\text.txt', 'w') as data:
#     data.write(g)




# def poly(k):
#     coeffs = [random.randint(0,5) for x in range(k+1)]
#     print(coeffs)
#     a = [f'{coeff}x!{k - num}' for num, coeff in enumerate(coeffs) if k - num == 1]
#     ham = [f'{coeff}x^{k - num}' for num, coeff in enumerate(coeffs) if coeff != 0 if num > 1]
#     data = list(zip(ham))
#     #b = [f'{coeff}X^{k - num}' for num, coeff in enumerate(coeffs) if coeff != 0 if num == 1]
#     return (data)



# print(poly(7))
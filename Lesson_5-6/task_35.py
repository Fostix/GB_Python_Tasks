# В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. 
# Найти его.

# with open(r'D:\GitHub\Python practic\GB_Tasks\Lesson_5-6\files\text_numbers.txt', 'w') as f:
#     for i in range(1,101):
#         f.write(f'{i} ')


with open(r'D:\GitHub\Python_practic\GB_Tasks\Lesson_5-6\files\text_numbers.txt', 'r') as f:
    find_num = f.read().split()
    L = [int(i) for i in find_num]
    for i in range(1, len(L)):
        if not L[i] - 1 == L[i-1]:
            print(L[i] - 1)
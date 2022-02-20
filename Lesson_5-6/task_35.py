# В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. 
# Найти его.

# with open('fil.txt', 'w') as f:
#     for i in range(1,101):
#         f.write(f'{i} ' '')


with open('fil.txt', 'r') as f:
    compr = [i for i in f.read(). split()]

    print(compr)
    for i in f:
        if not i == f:
            print(f)
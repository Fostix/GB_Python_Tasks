# Вычислить число  c заданной точностью d.
import  math


a = '0.01'#input('Enter float number: ')
test = False




if a[0] == '0':
    if a[1] == '.':
        i = 2
        while i < len(a) - 1:
            print(a[i])
            i += 1
            if a[i] == '1':
                test = True
    


if test == True:
    l = len(a) - 2
    print(round(math.pi, l))


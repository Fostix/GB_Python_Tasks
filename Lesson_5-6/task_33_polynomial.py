from random import randint

def Polynomial(k):
    str = []
    for i in range(0, k + 1):
        coeff = randint(0, 100)
        if i >= 2:
            str.append(f"{coeff}*x^{i} + ")
        elif i == 1:
            str.append(f"{coeff}*x + ")
        elif i == 0:
            str.append(f"{coeff} = 0")
    stroka = str[::-1]
    result = ''.join(stroka)
    with open(r"D:\GitHub\Python_practic\GB_Tasks\Lesson_5-6\files\task33_2.txt", "a") as data:
        data.write(result + '\n')
    
Polynomial(2)
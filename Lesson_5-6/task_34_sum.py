# Даны два файла в каждом из которых находится запись многочлена. Сформировать
# файл содержащий сумму многочленов.

with open(r'D:\GitHub\Python_practic\GB_Tasks\Lesson_5-6\files\task33.txt', 'r') as first_polynomial:
    first_polynomial = first_polynomial.readlines()[-1]


print()

with open(r"D:\GitHub\Python_practic\GB_Tasks\Lesson_5-6\files\task33_2.txt", "r") as second_file:
    second_polynomial = second_file.readlines()[-1]

variable_polynomial = []

equal_polynomial = first_polynomial.replace('=', '+')
equal_polynomial = equal_polynomial.replace('0', second_polynomial)
text = ' '
print(len(equal_polynomial))

#print(test[1:4])
for i in range(len(equal_polynomial)):
    if equal_polynomial[i] == '=':
        break
    while not equal_polynomial[i].isdigit() and equal_polynomial[i] != '^' and equal_polynomial[i] != '+' and equal_polynomial[i] != '*' and equal_polynomial[i] != ' ':
        text = equal_polynomial[i]
        i+=1
        if equal_polynomial[i] == '^':
            i+=1
            while equal_polynomial[i] != ' ':
                variable_polynomial.append(text + equal_polynomial[i])
                i+=1
        else:
                variable_polynomial.append(text)


print(variable_polynomial)
print(equal_polynomial)





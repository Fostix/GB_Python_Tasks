# Даны два файла в каждом из которых находится запись многочлена. Сформировать
# файл содержащий сумму многочленов.



from numpy import equal


def open_2_polynomial_files():
    with open(r'D:\GitHub\Python_practic\GB_Tasks\Lesson_5-6\files\task33.txt', 'r') as first_polynomial:
        first_polynomial = first_polynomial.readlines()[-1]

    with open(r"D:\GitHub\Python_practic\GB_Tasks\Lesson_5-6\files\task33_2.txt", "r") as second_file:
        second_polynomial = second_file.readlines()[-1]
    
    equal_polynomial = first_polynomial.replace('=', '+')
    equal_polynomial = equal_polynomial.replace('0', second_polynomial)
    return equal_polynomial




def feel_list(polynomial):
    text = ''
    variable_polynomial = []
    i = 0
    while polynomial[i] != '=':
        if polynomial[i] != '+' and polynomial[i] != ' ':
            text += polynomial[i]
        elif polynomial[i] == ' ' and text != '':
            variable_polynomial.append(text)
            text = ''
        i+=1
    return variable_polynomial


equal_polynomial = open_2_polynomial_files()
variable_polynomial = feel_list(equal_polynomial)


text = ''
for i in variable_polynomial:
    for k in i:
        if k.isdigit():

            k.replace(i, '')
            print(k)
            text += k

    print(text)




print(variable_polynomial)
print(equal_polynomial)




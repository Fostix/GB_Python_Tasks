# Даны два файла в каждом из которых находится запись многочлена. Сформировать
# файл содержащий сумму многочленов.



def open_2_polynomial_files():
    with open(r'D:\GitHub\Python_practic\GB_Tasks\Lesson_5-6\files\task33.txt', 'r') as first_polynomial:
        first_polynomial = first_polynomial.readlines()[-1]

    with open(r"D:\GitHub\Python_practic\GB_Tasks\Lesson_5-6\files\task33_2.txt", "r") as second_file:
        second_polynomial = second_file.readlines()[-1]
    
    equal_polynomial = first_polynomial.replace('=', '+')
    equal_polynomial = equal_polynomial.replace('0', second_polynomial)
    return equal_polynomial




def make(polynomial):
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









list_polynomial = []
coefficient_polynomial = []
text_pol = ''
text_coef = ''
check = False
for i in range(len(variable_polynomial)):
    if variable_polynomial[i].isdigit():
        coefficient_polynomial.append(variable_polynomial[i])
        list_polynomial.append('')
        continue
    for k in variable_polynomial[i]:
        print(k)
        if k.isdigit() and not check:
            text_coef += k
        elif not k.isdigit() or not check:
            check = True
            text_pol += k
        elif k.isdigit() and check:
            text_pol += k
    coefficient_polynomial.append(text_coef) # or i ?
    list_polynomial.append(text_pol)
    text_pol = ''
    text_coef = ''
    check = False








print(variable_polynomial)
print(equal_polynomial)
print(coefficient_polynomial)
print(list_polynomial)


# Даны два файла в каждом из которых находится запись многочлена. Сформировать
# файл содержащий сумму многочленов.



def open_file(way_file):
    with open(way_file, 'r') as file_polynomial:
        file_polynomial = file_polynomial.readlines()[-1]
    return file_polynomial


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





def function_shares_coefficients_and_polynomial(variable_polynomial):
    list_coefficient = []
    list_polynomial = []
    text_pol = ''
    text_coef = ''
    check = False
    for i in range(len(variable_polynomial)):
        if variable_polynomial[i].isdigit():
            list_coefficient.append(variable_polynomial[i])
            list_polynomial.append('')
            continue
        for k in variable_polynomial[i]:
            if k.isdigit() and not check:
                text_coef += k
            elif not k.isdigit() or not check:
                check = True
                text_pol += k
            elif k.isdigit() and check:
                text_pol += k
        if text_coef == '':
            text_coef = 0
        list_coefficient.append(text_coef)
        list_polynomial.append(text_pol)
        text_pol = ''
        text_coef = ''
        check = False
    return list_coefficient, list_polynomial
        




def sum_polynomial(list_coefficients, list_polynomial):
    coef_sum = []
    number = 0
    for i in range(len(list_polynomial) // 2):
        for k in range(len(list_coefficients)):
            if list_polynomial[i] == list_polynomial[k]:
                number += int(list_coefficients[k])
        if number == 0:
            coef_sum.append(list_polynomial[i])
        elif number != 0:
            coef_sum.append(str(number) + list_polynomial[i])
            number = int(number)
        number = 0
    return coef_sum






def main():
    way_first_file = r'D:\GitHub\Python_practic\GB_Tasks\Lesson_5-6\files\task33.txt'
    way_second_file = r'D:\GitHub\Python_practic\GB_Tasks\Lesson_5-6\files\task33_2.txt'


    string_first_polynomial = open_file(way_first_file)
    string_second_polynomial = open_file(way_second_file)


    equal_polynomial = string_first_polynomial.replace('=', '+')
    equal_polynomial = equal_polynomial.replace('0', string_second_polynomial)


    variable_polynomial = feel_list(equal_polynomial)


    list_coefficients, list_polynomial = function_shares_coefficients_and_polynomial(variable_polynomial)


    coef_sum = sum_polynomial(list_coefficients, list_polynomial)



    print(coef_sum)

main()
# В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19



numbers = [1.1, 1.2, 3.1, 5, 10.01]

max_number = 0
min_number = 9
for i in numbers:
    while i >= 1:
        i -= 1
    if max_number < i:
        max_number = i
    if min_number > i:
        min_number = i
    
print(max_number - min_number)










# print(round(1.5, 5))
# print(round(2.5, 5))
# print(round(3.5, 5))
# print(round(4.5, 5))


# math.modf(1.5)
# math.floor()



# def SaveFraction(number):
#     number = str(number)
#     check_point = False
#     fraction = ''
#     for i in range(len(number)):
#         if check_point == True:
#             fraction += number[i]
#             continue
#         if number[i] == '.':
#             check_point = True
#     if fraction == '':
#         return 5
#     return fraction





































# max_number = SaveFraction(numbers[0])
# min_number = SaveFraction(numbers[0])


# for i in numbers:
    
#     num = SaveFraction(i)
#     if max_number < num:
#         max_number = num
#     if min_number > num:
#         min_number = num

# print(min_number)



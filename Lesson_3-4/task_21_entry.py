# Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1


text_list = ["123", "234", 123, "567"]

never_count = 0
for i in range(len(text_list)):
    count = 0
    text_list[i] = str(text_list[i])
    for j in range(len(text_list)):
        text_list[j] = str(text_list[j])
        if i == j:
            continue
        if (text_list[i] in text_list[j]) == True:
            if j == len(text_list) - 1:
                print('position: -1')
                count +=1
            else:
                print(f'position: {j}')
                count +=1
                never_count += 1
    if count >= 1:
        print(f'count: {count}. word: {text_list[i]}')

if never_count == 0:
    print("don't element")

# останавливать ли поиск после нахождения одной копии?
# в примерах вроде ошибка

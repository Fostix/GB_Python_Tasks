# Определить, присутствует ли в заданном списке строк, некоторое число

here_text = ['Съешь ещё этих мягких французских булок, да выпей же чаю', 'Съешь ещё этих мяг6ких французских булок, да выпей 8же ча3ю', '343']
test_true = 0

for i in here_text:
    for j in i:
        if j.isdigit() == True:
            print('Да')
            test_true += 1
            break
    if j.isdigit() == True:
            break
if test_true == 0:
    print('нету')
# Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.
# Съешь ещё этих твердых китайских хлебушков, да выпей же какао
# Съешь ещё этих мягких французских булок, да выпей же чаю
mrText1 = 'Съешь ещё этих твердых китайских хлебушков, да выпей же какао.'
mrText2 = 'Съешь ещё этих мягких французских булок, да выпей же чаю.'
count = 0
length = mrText1

if len(mrText2) < len(mrText1):
    length = mrText2


for i in range(len(length)):
    if mrText1[i] == mrText2[i]:
        count += 1


print(count)

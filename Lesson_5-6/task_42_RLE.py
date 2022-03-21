# Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
# a. входные и выходные данные хранятся в отдельных текстовых файлах


text = 'adlhhhh hhsssssn'

col = 1

temp = ''


for i in range(1, len(text)):
    if text[i] == text[i - 1]:
        col +=1
    else:
        temp += str(col) + ':' + text[i - 1] + '-'
        col = 1
temp += str(col) + ':' + text[i]

print(temp)





# Найти НОК двух чисел.



# a = 12
# b = 37

a, b = map(int,input().split())
for_nod = a
temp = b
while temp>0:
    for_nod, temp = temp, for_nod%temp
print(for_nod)


nok = a * b / for_nod

print(nok)



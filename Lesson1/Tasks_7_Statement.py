# Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

list = [True, False]
result = True

for i in list:
    for j in list:
        for k in list:
            if not(list[i] or list[j] or list[k]) == (not list[i] and not list[j] and not list[k]):
                print(f'for X = {list[i]} for Y = {list[j]} for Z = {list[k]} - true')
            else:
                print(f'for X = {list[i]} for Y = {list[j]} for Z = {list[k]} - false')
                result = False
                break
        if not result:
            break
    if not result:
        break
if result:
    print(True)
else:
    print(False)

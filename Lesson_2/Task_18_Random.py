# Реализовать алгоритм перемешивания списка.


import time, random
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

random.shuffle(numbers)
print(numbers)


# for i in range(len(numbers)):
#     mixer = str(time.time())
#     mixer = int(mixer.replace('.', '')) % 100

#     while mixer > len(numbers) - 1:
#         mixer //= 2
#     numbers[i], numbers[mixer] = numbers[mixer], numbers[i]

# print(numbers)

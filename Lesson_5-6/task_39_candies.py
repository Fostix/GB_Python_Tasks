import random

candies = 27
max = 7
min = 1


while candies > 0:
    if candies > 0:
        bot = candies % (max + min)
        candies -= bot
        print(f'{candies} осталось')
        if candies == 0:
            print('you lose!')
    if candies > 0:
        candies -= int(input('you'))
        print(f'{candies} осталось')
        if candies == 0:
            print('you win!')




print(random.randint(0, 1))



























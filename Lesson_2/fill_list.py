import random

def fill_method(numbers_here, length):
    for i in range(length):
        numbers_here.append(random.randrange(10))
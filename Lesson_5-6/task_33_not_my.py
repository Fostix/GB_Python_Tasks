import random


def create_polynomial(number_k):
    max = 100
    coefficient = random.randint(0, max)
    if coefficient != 0:
        yield f'{coefficient}'

    coefficient = random.randint(0, max)
    if coefficient != 0:
        yield f'{coefficient}*x'

    for k in range(2, number_k + 1):
        coefficient = random.randint(0,max)
        if coefficient != 0:
            yield f'{coefficient}*x^{k}'

number_k = int(input('white number: '))
polynomial = list(create_polynomial(number_k))
polynomial.reverse()

data = open(r'file.txt', 'a')
data.write(polynomial[0])
for i in range(1, len(polynomial)):
    data.write(f' + {polynomial[i]}')
data.write(f' = 0\n')
data.close()
print(polynomial)
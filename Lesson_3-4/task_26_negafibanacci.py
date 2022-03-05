# Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов. 
# Т.е для k = 8, список будет выглядеть так: [-21 ,13, -8, 5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

def fib(n):
    if n >-1:
        if n == 0:
            return 0
        if n == 1:
            return 1
        else:
            return fib(n-1) + fib(n-2)
    if n <= -1:
        return (-1)**(n+1) * fib(-n)

a = int(input())
L = []
for i in range(-a, a+1):
    print(i)
    L.append(fib(i))
print(L)
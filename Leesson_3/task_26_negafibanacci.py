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
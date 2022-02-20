def fibonacci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci)

for i in range(1, 99999):
    print(fibonacci(i))
# Составить список простых множителей натурального числа N



# a = [ 2, 3, 5, 7, 11, 13, 17, 23, 29, 31 ]
# b = []

# number = int(input())

# index_a = -1
# while number != 1:    
#     while not number%a[index_a]:
#         index_a += 1
#         number /= a[index_a]
#     b.append(index_a)
#     index_a = -1


# print(b)

def Factor(n):
    Ans = []
    d = 2
    while d * d <= n:
        if not n % d:
            Ans.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        Ans.append(n)
    return Ans

print(Factor(9999999999999))
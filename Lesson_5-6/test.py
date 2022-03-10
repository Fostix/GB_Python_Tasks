# data = [x for x in range(10)]

# res = filter(lambda x: x%2 == 0, data)
# print(res)   # <filter object at 0x00...>

# data = [x for x in range(10)]

# res = list(filter(lambda x: not x%2, data))
# print(res)

# data = '1 2 3 5 8 15 23 38'.split()

# res = map(int, data)
# res = filter(lambda x: not x%2, res)
# res = list(map(lambda x:(x, x**2), res))
# print(res)
# i = 15

# while i < 10:
#     i += 1
#     print(i)


import turtle

turtle.shape('turtle')
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)

input()
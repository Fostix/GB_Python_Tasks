import math




def draw_table(table):
    row = int(math.sqrt(max(table)))
    for i in range(row):
        print(table[row * i: row * i + row])



table = list(range(1, 10))

draw_table(table)


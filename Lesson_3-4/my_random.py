from time import time




def my_rand():
    seed = time()
    a = 32310901
    b = 1729
    m = 20
    rOld = seed
    for i in range(9):
        rNew = (a*rOld + b) % m
        #print(rNew)
        rOld = rNew

my_rand()

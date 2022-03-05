# Написать программу преобразования десятичного числа в двоичное.

def binary(num):
    str_bin = ''
    bin_num = 0
    two = 2
    while num != 0:
        bin_num = num % two
        str_bin += str(bin_num)
        num //= two
    return int(str_bin[::-1])


number = 53
print(binary(number))
def bin():
    a = 3
    text = ''
    two = 2
    bin_num = 0
    while a != 0:
        bin_num = a % two
        text += str(bin_num)
        a //= two
    return(int(text[::-1]))

def gg(a):
	a = 3
	text = ''
	two = 2
	bin_num = 0
	while a != 0:
    	bin_num = a % two
    	text += str(bin_num)
    	a //= two
	return (int(text[::-1]))
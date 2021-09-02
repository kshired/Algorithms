from functools import reduce

def encrypt(numbers):
    numbers.sort()
    numbers[0] += 1

    res = reduce(lambda x,y :x*y,numbers)

    return res 

from itertools import permutations
from math import sqrt

def solve(n):
    if n <= 1:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n%i == 0:
            return False
    return True

def solution(numbers):
    perms = set()
    
    for i in range(1,len(numbers)+1):
        for value in permutations(numbers,i):
            perms.add(int(''.join(value)))
    
    perms = list(perms)
    
    cnt = 0
    
    for value in perms:
        if solve(value):
            cnt += 1
               
    return cnt
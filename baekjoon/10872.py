# https://acmicpc.net/problem/10872
# 팩토리얼

import sys
input = lambda : sys.stdin.readline().rstrip()

sys.setrecursionlimit(10**6)

def factorial(n):
    if n <= 1:
        return 1
    return n*factorial(n-1)

print(factorial(int(input())))
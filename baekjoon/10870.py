# https://acmicpc.net/problem/10870
# 피보나치 수 5

import sys
input = lambda : sys.stdin.readline().rstrip()

sys.setrecursionlimit(10**6)

def fibo(n):
    if n <= 1:
        return n 
    return fibo(n-1) + fibo(n-2)

print(fibo(int(input())))

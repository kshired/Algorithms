# https://acmicpc.net/problem/1676
# 팩토리얼 0의 개수

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())


N = int(input())

res = 0
mult = 5

while mult <= N:
    res += N//mult
    mult *= 5
    
print(res)
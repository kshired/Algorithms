# https://acmicpc.net/problem/1026
# 보물

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N = int(input())
A = list(input_multiple_int())
B = list(input_multiple_int())
res = 0

A.sort()
B.sort(reverse=True)

for i in range(N):
    res += A[i]*B[i]

print(res)
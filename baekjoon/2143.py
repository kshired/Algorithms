# https://acmicpc.net/problem/2143
# 두 배열의 합

import sys
from collections import defaultdict
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

T = int(input())
N = int(input())
arrA = list(input_multiple_int())
M = int(input())
arrB = list(input_multiple_int())

dA = defaultdict(int)
dB = defaultdict(int)

for i in range(N):
    for j in range(i,N):
        dA[sum(arrA[i:j+1])] += 1
    
for i in range(M):
    for j in range(i,M):
        dB[sum(arrB[i:j+1])] += 1

res = 0
for i in dA.keys():
    res += dB[T-i]*dA[i]

print(res)
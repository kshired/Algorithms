# https://acmicpc.net/problem/2003
# 수들의 합 2

import sys
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int,input().split())
arr = list(map(int,input().split()))

res = 0
sum = 0
l = 0
h = 0

while True:
    if sum >= M:
        sum -= arr[l]
        l += 1
    elif h == N:
        break
    else:
        sum += arr[h]
        h += 1
    if sum == M:
        res += 1

print(res)
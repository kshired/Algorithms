# https://acmicpc.net/problem/1744
# 수 묶기

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N = int(input())
values = []

for _ in range(N):
    values.append(int(input()))

values.sort()

l = 0
r = len(values)-1
res = 0

while l < r:
    if values[l] < 1 and values[l+1] < 1:
        res += values[l]*values[l+1]
    else:
        break
    l += 2

while r > 0:
    if values[r] > 1 and values[r-1] > 1:
        res += values[r]*values[r-1]
    else:
        break
    r -= 2

while l <= r:
    res += values[r]
    r -= 1

print(res)
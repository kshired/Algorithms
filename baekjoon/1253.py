# https://acmicpc.net/problem/1253
# 좋다

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N = int(input())
arr = list(input_multiple_int())
arr.sort()

res = 0

for i in range(N):
    tmp = arr[:i] + arr[i+1:]
    l = 0
    r = len(tmp) -1

    while l < r:
        s = tmp[l] + tmp[r]
        if s == arr[i]:
            res += 1
            break
        if s > arr[i]:
            r -= 1
        else:
            l += 1

print(res)
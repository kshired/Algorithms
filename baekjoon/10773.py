# https://acmicpc.net/problem/10773
# 제로

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

k = int(input())
arr = []

for _ in range(k):
    val = int(input())
    if val == 0:
        arr.pop()
    else:
        arr.append(val)

print(sum(arr))
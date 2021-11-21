# https://acmicpc.net/problem/10989
# 수 정렬하기 3

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

arr = [0 for _ in range(10001)]
N = int(input())

min = 10001
max = 0
for i in range(N):
    n = int(input())
    if n < min:
        min = n
    if n > max:
        max = n
    arr[n] += 1

for i in range(min, max+1):
    if arr[i] >= 1:
        for _ in range(arr[i]):
            print(i)


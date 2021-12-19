# https://acmicpc.net/problem/13300
# 방 배정

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

n,k = input_multiple_int()
arr = [[0,0] for _ in range(6)]

for _ in range(n):
    s,y = input_multiple_int()
    arr[y-1][s] += 1

cnt = 0

for female, male in arr:
    cnt += (female+k-1)//k
    cnt += (male+k-1)//k

print(cnt)
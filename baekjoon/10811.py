# https://acmicpc.net/problem/10811
# 바구니 뒤집기

import sys
input = lambda : sys.stdin.readline().rstrip()

N,M = map(int,input().split())
arr = [i for i in range(1,N+1)]
for _ in range(M):
    s,e = map(int,input().split())
    arr[s-1:e] = arr[-N+e-1:-N+s-2:-1]
for i in arr:
    print(i,end=' ')
print()
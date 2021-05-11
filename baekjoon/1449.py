# https://acmicpc.net/problem/1449
# 수리공 항승

import sys
input = lambda : sys.stdin.readline().rstrip()

N,L = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()

s,e = 0,1
cnt = 0

while e < N:
    if arr[e] - arr[s] < L:
        e += 1
    else:
        cnt += 1
        s = e
        e = s + 1
    
print(cnt+1)
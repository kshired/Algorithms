# https://acmicpc.net/problem/1715
# 카드 정렬하기

import sys
from heapq import heappush, heappop
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N = int(input())
hq = []

for _ in range(N):
    heappush(hq,int(input()))

if len(hq) == 1:
    print(0)
else:
    res = 0
    while len(hq) > 1:
        val1 = heappop(hq)
        val2 = heappop(hq)
        res += val1 + val2
        heappush(hq,val1+val2)        
    print(res)
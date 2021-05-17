# https://acmicpc.net/problem/11286
# 절댓값 힙

import sys
import heapq
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

hq = []

N = int(input())

for _ in range(N):
    val = int(input())
    if val:
        heapq.heappush(hq,(abs(val),val))
    else:
        if hq:
            print(heapq.heappop(hq)[1])
        else:
            print(0)
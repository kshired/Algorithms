# https://acmicpc.net/problem/11279
# 최대 힙

import sys
import heapq
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

hq = []

N = int(input())

for _ in range(N):
    val = int(input())
    if val:
        heapq.heappush(hq,-val)
    else:
        if hq:
            print(-heapq.heappop(hq))
        else:
            print(0)
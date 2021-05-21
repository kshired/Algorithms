# https://acmicpc.net/problem/1655
# 가운데를 말해요

import sys
from heapq import heappush, heappop
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N = int(input())
max_heap = []
min_heap = []
for _ in range(N):
    val = int(input())
    if len(max_heap) == len(min_heap):
        heappush(max_heap,-val)
    else:
        heappush(min_heap,val)
    if min_heap and -max_heap[0] > min_heap[0]:
        max_value = heappop(max_heap)
        min_value = heappop(min_heap)
        heappush(min_heap,-max_value)
        heappush(max_heap,-min_value)
    print(-max_heap[0])
# https://acmicpc.net/problem/7662
# 이중 우선순위 큐

import sys
from heapq import heappush, heappop
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

T = int(input())

for _ in range(T):
    K = int(input())
    max_heap = []
    min_heap = []
    visit = [True for _ in range(1000001)]
    for i in range(K):
        op,val = input().split()
        val = int(val)
        if op == 'I':
            heappush(max_heap,(-val,i))
            heappush(min_heap,(val,i))
            visit[i] = False
        else:
            if val == -1:
                while min_heap and visit[min_heap[0][1]]:
                    heappop(min_heap)
                if min_heap:
                    visit[min_heap[0][1]] = True
                    heappop(min_heap)
            else:
                while max_heap and visit[max_heap[0][1]]:
                    heappop(max_heap)
                if max_heap:
                    visit[max_heap[0][1]] = True
                    heappop(max_heap)
    
    while min_heap and visit[min_heap[0][1]]:
        heappop(min_heap)
    while max_heap and visit[max_heap[0][1]]:
        heappop(max_heap)
    if max_heap and min_heap:
        print(-max_heap[0][0],min_heap[0][0])
    else:
        print("EMPTY")
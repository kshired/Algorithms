# https://acmicpc.net/problem/2075
# N번째 큰 수

'''
min-heap을 이용하여 최대 N개까지만 들어 올 수 있게 유지.
마지막으로 N개가 들어있는 heap에서 pop을 하면 N번째로 큰 수가 pop.
'''

import sys
import heapq
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

hq = []

N = int(input())

for i in range(N):
    for val in input().split():
        heapq.heappush(hq,int(val))
        if len(hq) > N:
            heapq.heappop(hq)

print(heapq.heappop(hq))

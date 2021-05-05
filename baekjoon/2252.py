# https://www.acmicpc.net/problem/2252
# 줄 세우기
# 1766번이랑 완전 똑같은 문제.. 구현하고보니 코드가 똑같..;

import sys, heapq

input = lambda : sys.stdin.readline().rstrip()

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
in_degree = [0 for _ in range(N+1)]
pq = []

for _ in range(M):
    s,e = map(int,input().split())
    graph[s].append(e)
    in_degree[e] += 1

for i in range(1,N+1):
    if in_degree[i] == 0:
        heapq.heappush(pq,i)

while pq:
    poped = heapq.heappop(pq)
    print(poped,end = ' ')
    for i in graph[poped]:
        in_degree[i] -= 1
        if in_degree[i] == 0:
            heapq.heappush(pq,i)
# https://acmicpc.net/problem/1916
# 최소비용 구하기

import sys
import heapq

input = lambda : sys.stdin.readline().rstrip()
INF = 10e+9

N = int(input())
M = int(input())

hq = []
graph = [[] for _ in range(N+1)]
dist = [INF for _ in range(N+1)]

for _ in range(M):
    s,e,w = map(int,input().split())
    graph[s].append((e,w))

start,end = map(int,input().split())

heapq.heappush(hq,(0,start))

while hq:
    weight, now = heapq.heappop(hq)

    if weight > dist[now]:
        continue

    for i in graph[now]:
        nxt = i[0]
        nxtWeight = weight + i[1]
        if dist[nxt] > nxtWeight:
            dist[nxt] = nxtWeight
            heapq.heappush(hq,(nxtWeight,nxt))

print(dist[end])
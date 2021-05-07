# https://acmicpc.net/problem/1753
# 최단경로

import sys
import heapq

input = lambda : sys.stdin.readline().rstrip()

INF = 10e+9
V, E = map(int,input().split())
start = int(input())

graph = [[] for _ in range(V+1)]
dist = [0 for _ in range(V+1)]

for _ in range(E):
    s,e,w = map(int,input().split())
    graph[s].append((e,w))

for i in range(1,V+1):
    dist[i] = INF

dist[start] = 0
hq = []

heapq.heappush(hq,(0,start))

while hq:
    weight, now = heapq.heappop(hq)

    if weight > dist[now]:
        continue

    for i in graph[now]:
        nxt = i[0]
        nxtWeight = weight + i[1]
        if nxtWeight < dist[nxt]:
            dist[nxt] = nxtWeight
            heapq.heappush(hq,(nxtWeight,nxt))

for i in dist[1:]:
    if i == INF:
        print('INF')
    else:
        print(i)
# https://acmicpc.net/problem/11779
# 최소비용 구하기 2

import sys
import heapq

input = lambda : sys.stdin.readline().rstrip()
INF = 10e+9

N = int(input())
M = int(input())

hq = []
graph = [[] for _ in range(N+1)]
path = [0 for _ in range(N+1)] # 최단 경로 저장
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
            path[nxt] = now # now를 거쳐서 nxt로 가는 것이 최단 경로라면 path[nxt] = now로 해서 이전 정점 저장
            heapq.heappush(hq,(nxtWeight,nxt))

print(dist[end])

# 도착 정점에서 path 배열을 따라 역추적
res = []
while True:
    res.append(end)
    end = path[end]
    if end == start:
        res.append(end)
        break

print(len(res))

for i in res[::-1]:
    print(i,end=' ')
print()
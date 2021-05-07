# https://acmicpc.net/problem/1504
# 특정한 최단 경로

import sys
import heapq
input = lambda : sys.stdin.readline().rstrip()

INF = 10e+9

N,E = map(int,input().split())

graph = [[] for _ in range(N+1)]
dist = [INF for _ in range(N+1)]  # start -> other
dist1 = [INF for _ in range(N+1)] # v1 -> other
dist2 = [INF for _ in range(N+1)] # v2 -> other

def dijkstra(start, dist):
    dist[start] = 0
    hq = []
    heapq.heappush(hq,(0,start))
    while hq:
        weight, now = heapq.heappop(hq)
        
        if weight > dist[now]:
            continue

        for i in graph[now]:
            nxt, nxtWeight = i[0], i[1] + weight
            if dist[nxt] > nxtWeight:
                dist[nxt] = nxtWeight
                heapq.heappush(hq,(nxtWeight,nxt))


for _ in range(E):
    s,e,w = map(int,input().split())
    graph[s].append((e,w))
    graph[e].append((s,w))

v1, v2 = map(int, input().split())

dijkstra(1,dist)
dijkstra(v1,dist1)
dijkstra(v2,dist2)

# # start -> v1
# dist[v1]

# # start -> v2
# dist[v2]

# # v1 -> v2
# dist1[v2]

# # v2 -> v1
# dist2[v1]

# # v1 -> end
# dist1[N]

# # v2 -> end
# dist2[N]

# start -> v1 -> v2 -> end
distance1 = dist[v1] + dist1[v2] + dist2[N]

# start -> v2 -> v1 -> end
distance2 = dist[v2] + dist2[v1] + dist1[N]

res = min(distance1,distance2)

if res >= INF:
    print(-1)
else:
    print(res)
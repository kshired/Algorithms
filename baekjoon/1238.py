# https://acmicpc.net/problem/1238
# 파티

import sys
import heapq
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N,M,X = input_multiple_int()
graph = [[] for _ in range(N+1)]


for _ in range(M):
    u,v,w = input_multiple_int()
    graph[u].append((v,w))

res = []
comeback = []
for i in range(1,N+1):
    dist = [1e9+7 for _ in range(N+1)]
    hq = []
    dist[i] = 0
    heapq.heappush(hq,(0,i))
    
    while hq:
        weight,now = heapq.heappop(hq)
        
        if weight > dist[now]:
            continue

        for next in graph[now]:
            nxt,nxtWeight = next[0],weight+next[1]
            
            if dist[nxt] > nxtWeight:
                dist[nxt] = nxtWeight
                heapq.heappush(hq,(nxtWeight,nxt))

    if i == X:
        comeback = dist[1:]
    res.append(dist[X])

result = -1
for i in range(N):
    if comeback[i] + res[i] > result:
        result = comeback[i] + res[i]
print(result)
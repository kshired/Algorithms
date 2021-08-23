# https://programmers.co.kr/learn/courses/30/lessons/12978
# 배달
# 그냥 다익스트라 구현하기 ( 간선이 두 개 이상일때만 잘 처리해주면 된다. )

from heapq import heappush, heappop
def dijksra(V,graph,K):
    INF = K+1
    dist = [INF for _ in range(V+1)]
    
    dist[1] = 0
    
    hq = []
    
    heappush(hq,(0,1))
    
    while hq:
        weight, now = heappop(hq)
        
        if weight > dist[now]:
            continue
        
        for nxt,nxt_weight in graph[now].items():
            nxt_weight += weight
            if nxt_weight < dist[nxt]:
                dist[nxt] = nxt_weight
                heappush(hq,(nxt_weight,nxt))
    cnt = 0
    for i in dist[1:]:
        if i <= K:
            cnt += 1
    return cnt

def solution(N, road, K):
    graph = [dict() for _ in range(N+1)]
    
    for u,v,w in road:
        if graph[u].get(v):
            graph[u][v] = min(graph[u][v],w)
            graph[v][u] = min(graph[v][u],w)
        else:
            graph[u][v] = w
            graph[v][u] = w
    
    return dijksra(N, graph, K)

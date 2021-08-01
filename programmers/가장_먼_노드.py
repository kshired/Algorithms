from heapq import heappop, heappush

# https://programmers.co.kr/learn/courses/30/lessons/49189
# 가장 먼 노드

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    dist = [50001 for _ in range(n+1)]
    
    for u,v in edge:
        graph[u].append(v)
        graph[v].append(u)
    
    dist[1] = 0
    dist[0] = 0
    
    pq = []
    
    heappush(pq,1)
    
    while pq:
        now = heappop(pq)
        
        for nxt in graph[now]:
            if dist[nxt] == 50001 or dist[nxt] > dist[now] + 1:
                dist[nxt] = dist[now] + 1
                heappush(pq,nxt)
    
    answer = dist.count(max(dist))
    
    return answer
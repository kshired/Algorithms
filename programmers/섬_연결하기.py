# https://programmers.co.kr/learn/courses/30/lessons/42861
# 섬 연결하기
# 모든 경로의 최단거리 -> MST -> 크루스컬 or 프림 알고리즘을 구현

def solution(n, costs):
    graph = []
    for cost in costs:
        u,v,w = cost
        graph.append((w,u,v))
        graph.append((w,v,u))
    
    return kruskal(n,graph)

def find(v,parent):
    if v == parent[v]:
        return v
    else:
        u = find(parent[v],parent)
        parent[v] = u
    return u

def merge(u,v,parent,rank):
    u = find(u,parent)
    v = find(v,parent)
    if u == v:
        return True
    if rank[u] > rank[v]:
        u,v = v,u
    parent[u] = v
    if rank[u] == rank[v]:
        rank[v] += 1

def kruskal(n, graph):
    parent = [i for i in range(n+1)]
    rank = [1 for _ in range(n+1)]
    mst = []
    graph.sort()
    
    res = 0
    
    for w, u, v in graph:
        if find(u,parent) != find(v,parent):
            merge(u,v,parent,rank)
            res += w
    return res
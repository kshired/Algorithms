# https://acmicpc.net/problem/16202
# MST 게임

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

def find(v):
    if v == parent[v]:
        return v
    u = find(parent[v])
    parent[v] = u
    return u

def merge(u,v):
    u = find(u)
    v = find(v)
    if u == v:
        return
    if rank[u] > rank[v]:
        u,v = v,u
    parent[u] = v
    if rank[u] == rank[v]:
        rank[v] += 1

def kruskal():
    mst = []

    for w, u, v in graph:
        if find(u) != find(v):
            merge(u,v)
            mst.append(w)

    return mst

N,M,K = input_multiple_int()
graph = []
for i in range(M):
    u,v = input_multiple_int()
    graph.append((i+1,u,v))
    graph.append((i+1,v,u))

res = []
for i in range(K):
    parent = [i for i in range(N+1)]
    rank = [1 for _ in range(N+1)]
    mst = kruskal()
    if len(mst) != N-1:
        res.append(0)
    else:
        res.append(sum(mst))
    graph.pop(0)
    graph.pop(0)
print(*res)
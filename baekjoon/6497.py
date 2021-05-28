# https://acmicpc.net/problem/6497
# 전력난

import sys
from math import sqrt
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

def kruskal(graph):
    mst = []
    k = 0
    graph.sort()

    for w, u, v in graph:
        if find(u) != find(v):
            merge(u,v)
            mst.append(w)
        k += w

    return k//2-sum(mst)

while True:
    N,M = input_multiple_int()
    if N == 0 and M == 0:
        break
    parent = [i for i in range(N)]
    rank = [1 for _ in range(N)]
    graph = []
    for _ in range(M):
        u,v,w = input_multiple_int()
        graph.append((w,u,v))
        graph.append((w,v,u))
    print(kruskal(graph))

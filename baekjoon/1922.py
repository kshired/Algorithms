# https://acmicpc.net/problem/1922
# 네트워크 연결

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

def find(u):
    if u == parent[u]:
        return u
    v = find(parent[u])
    parent[u] = v
    return parent[u]

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
    graph.sort()

    for w,u,v in graph:
        if find(u) != find(v):
            merge(u,v)
            mst.append(w)

    return sum(mst)

N = int(input())
M = int(input())

parent = [i for i in range(N+1)]
rank = [1 for _ in range(N+1)]
graph = []

for _ in range(M):
    u,v,w = input_multiple_int()
    graph.append((w,u,v))
    graph.append((w,v,u))

print(kruskal(graph))

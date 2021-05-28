# https://acmicpc.net/problem/2887
# 행성 터널

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
    mst = 0
    graph.sort()

    for w,u,v in graph:
        if find(u) != find(v):
            merge(u,v)
            mst += w

    return mst

N = int(input())

parent = [i for i in range(N+1)]
rank = [1 for _ in range(N+1)]
pos = []
graph = []

for i in range(N):
    pos.append(list(input_multiple_int())+[i])

for i in range(3):
    pos.sort(key=lambda x:x[i])
    for j in range(1,N):
        graph.append((abs(pos[j-1][i]-pos[j][i]),pos[j-1][3],pos[j][3]))

print(kruskal(graph))
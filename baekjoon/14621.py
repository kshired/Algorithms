# https://acmicpc.net/problem/14621
# 나만 안되는 연애

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
    graph.sort()

    for w, u, v in graph:
        if find(u) != find(v):
            merge(u,v)
            mst.append(w)

    return mst

N,M = input_multiple_int()
parent = [i for i in range(N+1)]
rank = [1 for _ in range(N+1)]
sex = input().split()
graph = []

for _ in range(M):
    u,v,w = input_multiple_int()
    if sex[u-1] != sex[v-1]:
        graph.append((w,u,v))
        graph.append((w,v,u))

res = kruskal()
if len(res) != N-1:
    print(-1)
else:
    print(sum(res))
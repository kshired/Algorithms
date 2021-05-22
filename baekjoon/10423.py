# https://acmicpc.net/problem/10423
# 전기가 부족해

'''
MST를 구하는 문제.
모든 도시 그룹은 하나의 발전소만 연결되어야함.
그냥 발전소를 다 merge해서 하나 이상 연결하면 cycle이 생긴 것이라 판단하게 하자!
그 후 kruskal을 통해 mst 구성하면 끝!
'''

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N,M,K = input_multiple_int()
parent = [i for i in range(N+1)]
rank = [1 for _ in range(N+1)]

def find(u):
    if u == parent[u]:
        return u
    else:
        v = find(parent[u])
        parent[u] = v
        return v

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
    graph.sort(key=lambda x:x[2])

    for u,v,w in graph:
        if find(u) != find(v):
            merge(u,v)
            mst.append(w)

    return mst

graph = []
for i in input().split():
    merge(0,int(i))

for _ in range(M):
    graph.append(list(input_multiple_int()))

res = kruskal(graph)

print(sum(res))
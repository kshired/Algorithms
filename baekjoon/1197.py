# https://acmicpc.net/problem/1197
# 최소 스패닝 트리

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

def find(v):
	if v == parent[v]:
		return v
	else:
		u = find(parent[v])
		parent[v] = u
		return u

def merge(u, v):
	u = find(u)
	v = find(v)
	if u == v:
		return True
	if rank[u] > rank[v]:
		u,v = v,u
	parent[u] = v
	if rank[u] == rank[v]:
		rank[v] += 1

def kruskal(graph):
    res = 0
    graph.sort(key=lambda x:x[2])

    for u, v, w in graph:
        if find(u) != find(v):
            merge(u,v)
            res += w
    
    return res

N,M = input_multiple_int()
parent = [i for i in range(N+1)]
rank = [1 for _ in range(N+1)]
graph = []

for _ in range(M):
    graph.append(list(input_multiple_int()))

print(kruskal(graph))
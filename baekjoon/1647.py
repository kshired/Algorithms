# https://acmicpc.net/problem/1647
# 도시 분할 계획

'''
도시를 2개로 분할하기 위해,
MST를 구성한후 weight가 가장 큰 간선을 끊는다.

-> MST를 만들고, 마지막 간선만 제외시킨다.
'''

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N,M = input_multiple_int()
parent = [i for i in range(N+1)]
rank = [1 for _ in range(N+1)]

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
    mst = []
    graph.sort()
    for w, u, v in graph:
        if find(u) != find(v):
            merge(u,v)
            mst.append(w)
    
    return mst

graph = []
for _ in range(M):
    a,b,w = input_multiple_int()
    graph.append([w,a,b])

res = kruskal(graph)
print(sum(res[:-1]))
# https://acmicpc.net/problem/4386
# 별자리 만들기

'''
그냥! MST를 잘 만들어보자!
'''

import sys
from math import sqrt
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N = int(input())
parent = [i for i in range(N)]
rank = [1 for _ in range(N)]
points = []
graph = []

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

    return sum(mst)

for _ in range(N):
    points.append(list(map(float,input().split())))

for i in range(N):
    for j in range(N):
        if i!=j:
            distance = sqrt((points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2)
            graph.append((distance,i,j))
            graph.append((distance,j,i))
    
print("%.2f"%(kruskal()))
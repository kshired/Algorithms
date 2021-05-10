# https://acmicpc.net/problem/1717
# 집합의 표현

import sys
input = lambda : sys.stdin.readline().rstrip()

n,m = map(int,input().split())

parent = [i for i in range(n+1)]
rank = [i for i in range(n+1)]

def find(v):
    if v == parent[v]:
        return v
    else:
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

for _ in range(m):
    op, a, b = map(int,input().split())
    if op:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
    else:
        merge(a,b)

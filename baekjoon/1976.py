# https://acmicpc.net/problem/1976
# 여행 가자

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

N = int(input())
M = int(input())

parent = [i for i in range(N+1)]
rank = [1 for _ in range(N+1)]

values = []
for _ in range(N):
    values.append(list(input_multiple_int()))

for i in range(N):
    for j in range(N):
        if values[i][j] == 1:
            merge(i+1,j+1)
    
path = list(input_multiple_int())

for i in range(M):
    if i == 0:
        prev = path[i]
    else:
        if find(path[i]) == find(prev):
            prev = path[i]
        else:
            print("NO")
            break
else:
    print("YES")

    
# https://acmicpc.net/problem/2162
# 선분 그룹

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

def ccw(a,b,c):
    op = a[0]*b[1] + b[0]*c[1] + c[0]*a[1]
    op -= (a[1]*b[0] + b[1]*c[0] + c[1]*a[0])
    if op > 0:
        return 1
    elif op == 0:
        return 0
    else:
        return -1

def isIntersect(x,y):
    a = x[0]
    b = x[1]
    c = y[0]
    d = y[1]
    ab = ccw(a,b,c)*ccw(a,b,d)
    cd = ccw(c,d,a)*ccw(c,d,b)
    if ab == 0 and cd == 0:
        if a > b:
            a,b = b,a
        if c > d:
            c,d = d,c
        if a <= d and c <= b:
            return True
        else:
            return False
    else:
        if ab <= 0 and cd <= 0:
            return True
        else:
            return False

def find(u):
    if u == parent[u]:
        return u
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

N = int(input())
d = dict()
parent = [i for i in range(N)]
rank = [1 for i in range(N)]

for i in range(N):
    x1,y1,x2,y2= input_multiple_int()
    d[i] = [(x1,y1),(x2,y2)]

for i in range(N-1):
    for j in range(i+1,N):
        if isIntersect(d[i],d[j]):
            merge(i,j)

res = [0 for _ in range(N)]
cnt = 0
for i in range(N):
    if parent[i] == i:
        cnt += 1
    res[find(i)] += 1

print(cnt)
print(max(res))
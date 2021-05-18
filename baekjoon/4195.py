# https://acmicpc.net/problem/4195
# 친구 네트워크

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

def merge(u,v):
    u = find(u)
    v = find(v)
    if u == v:
        return
    parent[u] = v
    count[v] += count[u]

T = int(input())

for _ in range(T):
    count = dict()
    parent = dict()
    N = int(input())
    for i in range(N):
        a,b = input().split()
        if a not in parent:
            parent[a] = a
            count[a] = 1
        if b not in parent:
            parent[b] = b
            count[b] = 1
        merge(a,b)
        print(count[find(b)])

        

# https://acmicpc.net/problem/1043
# 거짓말

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

N,M = input_multiple_int()

parent = [i for i in range(N+1)]
rank = [1 for _ in range(N+1)]

trues = list(input_multiple_int())[1:]

parties = []
for _ in range(M):
    party = list(input_multiple_int())[1:]
    parties.append(party)
    for i in party:
        for j in party:
            merge(i,j)

cnt = 0
for party in parties:
    for person in party:
        for i in range(1,N+1):
            if i in trues and find(i) == find(person):
                break
        else:
            continue
        break
    else:
        cnt += 1
print(cnt)
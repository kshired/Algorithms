# https://acmicpc.net/problem/16562
# 친구비

'''
union find를 이용해 disjoint-set을 만들고,
각 disjoint-set의 최소 친구비를 정하여
그것을 전부 더한 뒤 K값과 비교해주면 됨.
'''

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N,M,K = input_multiple_int()
parent = [i for i in range(N)]
rank = [1 for _ in range(N)]
money = list(input_multiple_int())

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

for _ in range(M):
    u,v = input_multiple_int()
    merge(u-1,v-1)

for i in range(N):
    if parent[i] != i:
        u = find(i)
        money[u] = min(money[u],money[i])

tot = 0
for i in range(N):
    if parent[i] == i:
        tot += money[i]
    
if tot <= K:
    print(tot)
else:
    print("Oh no")

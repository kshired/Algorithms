# https://www.acmicpc.net/problem/20303
# 할로윈의 양아치

'''
disjoint-set + dp

그룹 잘 나누고, 냅색문제와 똑같은 점화식으로 dp를하면 된다.

'''

import sys
from collections import defaultdict

input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N,M,K = input_multiple_int()

parent = [i for i in range(N)]
rank = [1 for _ in range(N)]

candy = list(input_multiple_int())

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
    s,e = input_multiple_int()
    merge(s-1,e-1)

d = defaultdict(lambda: [0,0])
for idx,val in enumerate(parent):
    d[find(val)][0] += 1
    d[find(val)][1] += candy[idx] 

# [사람 인원수, candy 수]
group = [i for i in d.values()]

dp = [[0 for _ in range(K)] for _ in range(len(group))]

for i in range(len(group)):
    for j in range(K):
        if group[i][0] <= j:
            dp[i][j] = max(group[i][1]+dp[i-1][j-group[i][0]],dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[-1][K-1])
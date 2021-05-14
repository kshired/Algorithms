# https://acmicpc.net/problem/1967
# 트리의 지름

import sys
sys.setrecursionlimit(10**7)
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    values = list(input_multiple_int())
    graph[values[0]].append((values[1],values[2]))
    graph[values[1]].append((values[0],values[2]))


def dfs(start, now, res):
    for node, weight in graph[now]:
        if res[node] == 0 and node != start:
            res[node] = res[now] + weight
            dfs(now, node, res)

res1 = [0 for _ in range(N+1)]
res2 = [0 for _ in range(N+1)]

dfs(1,1,res1)
res1[1] = 0

maximum = 0
idx = 0

for i in range(N+1):
    if maximum < res1[i]:
        maximum = res1[i]
        idx = i

dfs(idx, idx, res2)
res2[idx] = 0
print(max(res2))
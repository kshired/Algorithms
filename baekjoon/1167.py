# https://acmicpc.net/problem/1167
# 트리의 지름

'''
트리의 지름은 임의의 정점 x에서 최장거리의 노드 y를 구한 후
y에서 최장거리의 노드 z를 구했을 때,

y부터 z까지의 거리이다.

따라서 임의의 점에서 dfs를 진행하고,
그 후 가장 거리가 먼 노드에서부터 dfs를 다시 진행한 뒤,
가장 거리가 먼 노드까지의 거리를 구하면 된다.
'''

import sys
sys.setrecursionlimit(10**7)
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N):
    values = list(input_multiple_int())
    start = values[0]
    for i in range(1,len(values[1:-1]),2):
        graph[start].append((values[i],values[i+1]))

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

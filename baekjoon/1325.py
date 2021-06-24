# https://acmicpc.net/problem/1325
# 효율적인 해킹

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N,M = input_multiple_int()
graph = [[] for _ in range(N)]

for _ in range(M):
    u,v = input_multiple_int()
    graph[v-1].append(u-1)

def dfs(u):
    stack = [u]
    visit = [False for _ in range(N)]

    visit[u] = True
    
    cnt = 0

    while stack:
        now = stack.pop()
        cnt += 1
        for next in graph[now]:
            if not visit[next]:
                visit[next] = True
                stack.append(next)
    
    return cnt

res = []
for i in range(N):
    res.append(dfs(i))

max_value = max(res)

for i in range(N):
    if res[i] == max_value:
        print(i+1,end=" ")
print()

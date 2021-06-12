# https://acmicpc.net/problem/1389
# 케빈 베이컨의 6단계 법칙

import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

def bfs(u,v,size):
    q = deque()
    visit = [False for _ in range(size+1)]
    visit[u] = True
    q.append((u,0))

    while q:
        cur,cnt = q.popleft()
        if cur == v:
            return cnt

        for next in graph[cur]:
            if not visit[next]:
                visit[next] = True
                q.append((next,cnt+1))

N,M = input_multiple_int()
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u,v = input_multiple_int()
    graph[u].append(v)
    graph[v].append(u)

res = []
for i in range(1,N+1):
    tmp = 0
    for j in range(1,N+1):
        if i == j:
            continue
        tmp += bfs(i,j,N)
    res.append(tmp)

for i in range(N):
    if res[i] == min(res):
        print(i+1)
        break
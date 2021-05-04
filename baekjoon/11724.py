# https://www.acmicpc.net/problem/11724
# 연결 요소의 개수

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

def bfs(v):
    q = deque()
    q.append(v)
    visit[v] = 1
    while q:
        v = q.popleft()
        for i in graph[v]:
            if visit[i] == 0:
                visit[i] = 1
                q.append(i)

N,M = map(int,input().split())
graph = [[] for _ in range(N)]
visit = [0 for _ in range(N)]

for _ in range(M):
    u,v = map(int,input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)



cnt = 0

for i in range(N):
    if visit[i] == 0:
        bfs(i)
        cnt += 1

print(cnt)
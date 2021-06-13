# https://acmicpc.net/problem/1240
# 노드사이의 거리

import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N,M = input_multiple_int()
graph = [[] for _ in range(N)]

for _ in range(N-1):
    u,v,w = input_multiple_int()
    graph[u-1].append((v-1,w))
    graph[v-1].append((u-1,w))

def bfs(s,e):
    visit = [False for _ in range(N)]
    q = deque()

    q.append((s,0))
    visit[s] = True

    while q:
        u,w = q.popleft()
        if u == e:
            return w

        for next in graph[u]:
            if not visit[next[0]]:
                q.append((next[0],w+next[1]))
                visit[next[0]] = True

for _ in range(M):
    u,v = input_multiple_int()
    print(bfs(u-1,v-1))
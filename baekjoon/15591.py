# https://acmicpc.net/problem/15591
# MooTube (Silver)

import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N,Q = input_multiple_int()

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    u,v,w = input_multiple_int()
    graph[u].append((v,w))
    graph[v].append((u,w))

for _ in range(Q):
    k,v = input_multiple_int()
    
    visit = [False for _ in range(N+1)]
    visit[v] = True

    q = deque()
    q.append(v)
    res = 0
    while q:
        now = q.popleft()
        for next,weight in graph[now]:
            if not visit[next]:
                if weight >= k:
                    res += 1
                    visit[next] = True
                    q.append(next)
    print(res)
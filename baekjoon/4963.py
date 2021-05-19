# https://acmicpc.net/problem/4963
# 섬의 개수

import sys
from collections import defaultdict
sys.setrecursionlimit(10**7)
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

dir = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]


def dfs(y,x,graph,visit):
    visit[y][x] = True

    for i in range(8):
        ny,nx = y + dir[i][0], x + dir[i][1]
        if 0 <= ny < M and 0 <= nx < N:
            if not visit[ny][nx] and graph[ny][nx]:
                dfs(ny,nx,graph,visit)

while True:
    N,M = input_multiple_int()

    if N + M == 0:
        break

    graph = []
    visit = [[False for _ in range(N)] for _ in range(M)]

    for i in range(M):
        graph.append(list(input_multiple_int()))

    res = 0
    for i in range(M):
        for j in range(N):
            if not visit[i][j] and graph[i][j]:
                res += 1
                dfs(i,j,graph,visit)
    print(res)
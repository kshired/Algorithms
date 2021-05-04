# https://www.acmicpc.net/problem/1012
# 유기농 배추
import sys
sys.setrecursionlimit(10**6)

def dfs(y,x):
    global graph, cnt
    for i in range(4):
        ny,nx = y+dy[i],x+dx[i]
        if (0 <= ny < N) and (0 <= nx < M):
            if graph[ny][nx] == 1:
                cnt += 1
                graph[ny][nx] = 0
                dfs(ny,nx)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N = int(input())

for _ in range(N):
    M,N,K = map(int, input().split())
    graph = [[0 for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        x,y = map(int,input().split())
        graph[y][x] = 1

    res = []
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j]:
                dfs(i,j)
                res.append(cnt if cnt else 1)
                graph[i][j] = 1
            cnt = 0
    print(len(res))

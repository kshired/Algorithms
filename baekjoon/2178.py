# https://www.acmicpc.net/problem/2178
# 미로탐색

from collections import deque

N,M = map(int,input().split())

graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for _ in range(N):
    graph.append(list(map(int,input())))


def bfs(y,x):
    visit = [[0 for _ in range(M)] for _ in range(N)]
    q = deque()
    q.append((y,x))
    visit[y][x] = 1

    while q:
        y,x = q.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if (0 <= new_x < M) and (0 <= new_y < N):
                if graph[new_y][new_x] == 1 and visit[new_y][new_x] == 0:
                    graph[new_y][new_x] = graph[y][x] + 1
                    q.append((new_y,new_x))

bfs(0,0)
print(graph[N-1][M-1])
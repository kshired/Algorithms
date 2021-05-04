# https://www.acmicpc.net/problem/10026
# 적록색약

from collections import deque

def bfs(y,x,val,graph):
    global cnt
    q = deque()
    q.append((y,x))
    while q:
        y,x = q.popleft()
        for i in range(4):
            ny,nx = y+dy[i],x+dx[i]
            if (0<=ny<N) and (0<=nx<N):
                if graph[ny][nx] == val:
                    graph[ny][nx] = ''
                    cnt += 1
                    q.append((ny,nx))

N = int(input())
graph = []
graph2 = []
res = []
values = ['R','B','G']

dx = [-1,0,1,0]
dy = [0,-1,0,1]

for _ in range(N):
    tmp = list(input())
    graph.append(tmp)
    graph2.append(list(map(lambda x: x if x=='R' or x=='B' else 'R',tmp)))

for val in values:
    cnt = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] == val:
                bfs(i,j,val,graph)
                res.append(cnt if cnt else 1)
        cnt = 0

print(len(res),end=' ')

res = []

for val in values[:2]:
    cnt = 0
    for i in range(N):
        for j in range(N):
            if graph2[i][j] == val:
                bfs(i,j,val,graph2)
                res.append(cnt if cnt else 1)
        cnt = 0

print(len(res))
# https://www.acmicpc.net/problem/2667
# 단지번호 붙이기

N = int(input())

graph = []
for _ in range(N):
    graph.append(list(map(int,input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0
res = []

def dfs(y,x):
    global graph, cnt

    for i in range(4):
        ny,nx = y+dy[i],x+dx[i]
        if (0 <= ny < N) and (0 <= nx < N):
            if graph[ny][nx] == 1:
                cnt += 1
                graph[ny][nx] = 0
                dfs(ny,nx)

for i in range(N):
    for j in range(N):
        if graph[i][j]:
            dfs(i,j)
            res.append(cnt if cnt else 1)
        cnt = 0

res.sort()
print(len(res))
for i in res:
    print(i)
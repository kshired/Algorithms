# https://www.acmicpc.net/problem/2606
# 바이러스

N = int(input())
M = int(input())
graph = [[0 for _ in range(N)] for _ in range(N)]
visit = [0 for _ in range(N)]
ans = 0
for _ in range(M):
    s,e = map(int,input().split())
    graph[s-1][e-1] = 1
    graph[e-1][s-1] = 1

def dfs(v):
    global graph, visit, ans
    ans += 1
    visit[v] = 1
    for i in range(N):
        if graph[v][i] == 1 and visit[i] == 0:
            dfs(i)

dfs(0)
print(ans-1)
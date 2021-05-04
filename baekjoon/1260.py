# https://www.acmicpc.net/problem/1260
# DFS와 BFS

from collections import deque

def dfs(v):
    global graph,visit
    visit[v] = 1
    print(v,end=' ')
    for i in range(1,N+1):
        if graph[v][i] == 1 and visit[i] == 0:
            dfs(i)

def bfs(v):
    global graph,q,visit
    visit[v] = 1
    print(v,end=' ')
    q.append(v)
    while q:
        v = q.popleft()
        for i in range(1,N+1):
            if graph[v][i] == 1 and visit[i] == 0:
                visit[i] = 1
                print(i, end=' ')
                q.append(i)


N,M,V = map(int,input().split())
graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
visit = [0 for _ in range(N+1)]
q = deque()



for _ in range(M):
    s,e = map(int,input().split())
    graph[s][e] = 1
    graph[e][s] = 1

dfs(V)
print()
visit = [0 for _ in range(N+1)]
bfs(V)
print()
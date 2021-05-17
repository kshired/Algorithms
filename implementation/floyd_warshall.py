INF = 1e9+7
N = 100
graph = [[INF for in range(N)] for _ in range(N)]

def floyd_warshall(graph):
    for i in range(N):
        graph[i][i] = 0

    for k in range(N):
        for i in range(N):
            for j in range(N):
                graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])

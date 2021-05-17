# https://acmicpc.net/problem/1613
# 역사

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N,M = input_multiple_int()
graph = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(M):
    a,b = input_multiple_int()
    graph[a-1][b-1] = -1
    graph[b-1][a-1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][k] == graph[k][j] and graph[i][k] + graph[k][j] != 0:
                graph[i][j] = graph[i][k]

K = int(input())
for i in range(K):
    a,b = input_multiple_int()
    print(graph[a-1][b-1])
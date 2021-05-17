# https://acmicpc.net/problem/10159
# 저울

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N = int(input())
M = int(input())
graph = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(M):
    a,b = input_multiple_int()
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = -1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][k] == graph[k][j] and graph[i][k] + graph[k][j] != 0:
                graph[i][j] = graph[i][k]


for i in range(N):
    print(graph[i].count(0)-1)

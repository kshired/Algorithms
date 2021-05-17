# https://acmicpc.net/problem/11404
# 플로이드

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())
INF = 1e9+7

N = int(input())
M = int(input())

graph = [[INF for _ in range(N)] for _ in range(N)]

for _ in range(M):
    a,b,c = input_multiple_int()
    graph[a-1][b-1] = min(graph[a-1][b-1],c)

for i in range(N):
    graph[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])

for i in graph:
    for j in i:
        if j == INF:
            print(0,end=' ')
        else:
            print(j,end=' ')
    print()


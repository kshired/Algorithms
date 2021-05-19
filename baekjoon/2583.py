# https://acmicpc.net/problem/2583
# 영역 구하기

import sys
sys.setrecursionlimit(10**7)
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

dir = [(0,1),(0,-1),(1,0),(-1,0)]

def dfs(y,x):
    res = 1
    visit[y][x] = True
    for i in range(4):
        ny,nx = y + dir[i][0], x + dir[i][1]
        if 0 <= ny < M and 0 <= nx < N:
            if not visit[ny][nx] and graph[ny][nx]:
                res += dfs(ny,nx)
    return res

M,N,K = input_multiple_int()

graph = [[1 for _ in range(N)] for _ in range(M)]
visit = [[False for _ in range(N)] for _ in range(M)]

for _ in range(K):
    s1,e1,s2,e2 = input_multiple_int()
    for i in range(e1,e2):
        for j in range(s1,s2):
            graph[i][j] = 0

res = []
for i in range(M):
    for j in range(N):
        if not visit[i][j] and graph[i][j]:
            res.append(dfs(i,j))

res.sort()
print(len(res))
for i in res:
    print(i,end=' ')
print()
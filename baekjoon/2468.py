# https://acmicpc.net/problem/2468
# 안전 영역

import sys
sys.setrecursionlimit(10**7)
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N = int(input())
in_range = lambda y,x: 0 <= y < N and 0 <= x < N

def dfs(y,x,val):
    visit[y][x] = True
    for i in range(4):
        ny, nx = y + dir[i][0], x + dir[i][1]
        if in_range(ny,nx):
            if not visit[ny][nx] and graph[ny][nx] > val:
                dfs(ny,nx,val)

graph = []
dir = [(0,1),(0,-1),(1,0),(-1,0)]

max_val = 0
for _ in range(N):
    values = list(input_multiple_int())
    max_val = max(max_val,max(values))
    graph.append(values)

res = 0
for i in range(0,max_val+1):
    visit = [[False for _ in range(N)] for _ in range(N)]
    cnt = 0
    for j in range(N):
        for k in range(N):
            if not visit[j][k] and graph[j][k] > i:
                cnt += 1
                dfs(j,k,i)
    res = max(res,cnt)
print(res)
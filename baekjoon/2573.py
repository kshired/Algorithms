# https://acmicpc.net/problem/2573
# 빙산

'''
구역을 나누는 문제.

빙하를 녹일 때 한꺼번에 다같이 녹여야하는데,
각각 녹여서 문제 생겼음.
python3로 속도가 안나와서 pypy3로 제출함.

'''
import sys
sys.setrecursionlimit(10**4)
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N,M = input_multiple_int()
in_range = lambda y,x: 0 <= y < N and 0 <= x < M

def dfs(y,x):
    visit[y][x] = True
    cnt = 0
    for i in range(4):
        ny, nx = y + dir[i][0], x + dir[i][1]
        if in_range(ny,nx):
            if graph[ny][nx] == 0:
                cnt += 1
            if not visit[ny][nx] and graph[ny][nx]:
                dfs(ny,nx)
    if graph[y][x] > cnt:
        graph[y][x] -= cnt
    else:
        graph[y][x] = -1

graph = []
dir = [(0,1),(0,-1),(1,0),(-1,0)]

for _ in range(N):
    values = list(input_multiple_int())
    graph.append(values)

idx = 0
while True:
    visit = [[False for _ in range(M)] for _ in range(N)]
    cnt = 0
    for j in range(N):
        for k in range(M):
            if not visit[j][k] and graph[j][k]:
                cnt += 1
                dfs(j,k)
    
    if cnt == 0:
        print(0)
        break
    
    if cnt > 1:
        print(idx)
        break
    
    for j in range(N):
        for k in range(M):
            if graph[j][k] == -1:
                graph[j][k] = 0
    
    idx += 1
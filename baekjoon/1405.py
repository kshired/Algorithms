# https://acmicpc.net/problem/1405
# 미친 로봇

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

values = list(input_multiple_int())
N = values[0]
chances = list(map(lambda x:x/100,values[1:]))
visit = [[False for _ in range(2*N+1)] for _ in range(2*N+1)]
dir = [(1,0),(-1,0),(0,-1),(0,1)]

def dfs(y,x,cnt):
    if cnt == N:
        return 1

    visit[y][x] = True
    res = 0
    for i in range(4):
        dy, dx = y + dir[i][0], x + dir[i][1]
        if not visit[dy][dx]:
            res += dfs(dy,dx,cnt+1)*chances[i]
    visit[y][x] = False
    return res

print(dfs(N,N,0))
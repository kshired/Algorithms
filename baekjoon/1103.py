# https://acmicpc.net/problem/1103
# 게임

import sys
sys.setrecursionlimit(10**5)
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N,M = input_multiple_int()
board = []

for _ in range(N):
    board.append(list(input()))

res = []
visit = [[False for _ in range(M)] for _ in range(N)]
dp = [[-1 for _ in range(M)] for _ in range(N)]
dir = [(1,0),(-1,0),(0,1),(0,-1)]
chk = False
def dfs(y,x):
    global chk
    if 0 <= y < N and 0 <= x < M:
        if board[y][x] == 'H':
            return 0

        if visit[y][x]:
            chk = True
            return -1

        if dp[y][x] != -1:
            return dp[y][x]
        
        visit[y][x] = True
        cur = int(board[y][x])
        for d in dir:
            dy,dx = y + d[0] * cur, x + d[1] * cur
            dp[y][x] = max(dp[y][x],dfs(dy,dx)+1)
        visit[y][x] = False

        return dp[y][x]
    else:
        return 0

res = dfs(0,0)

if chk:
    print(-1)
else:
    print(res)
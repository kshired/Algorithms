# https://acmicpc.net/problem/14502
# 연구소

import sys
from copy import deepcopy
from collections import deque
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N,M = input_multiple_int()
board = []
for _ in range(N):
    board.append(list(input_multiple_int()))

dir = [(0,1),(0,-1),(1,0),(-1,0)]
ans = 0

def bfs():
    global ans
    tmp = deepcopy(board)
    q = deque()
    for i in range(N):
        for j in range(M):
            if tmp[i][j] == 2:
                q.append((i,j))
    
    while q:
        y,x = q.popleft()
        for i in range(4):
            ny,nx = y+dir[i][0],x+dir[i][1]
            if 0 <= ny < N and 0 <= nx < M and tmp[ny][nx] == 0:
                tmp[ny][nx] = 2
                q.append((ny,nx))
    
    cnt = 0
    for i in tmp:
        for j in i:
            if j == 0:
                cnt += 1

    ans = max(ans,cnt)


def solve(n):
    if n == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                board[i][j] = 1
                solve(n+1)
                board[i][j] = 0    
    
solve(0)
print(ans)
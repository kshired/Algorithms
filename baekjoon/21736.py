# https://acmicpc.net/problem
# 헌내기는 친구가 필요해

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N,M = input_multiple_int()
board = []

for _ in range(N):
    board.append(list(input()))

sy,sx = -1,-1
for i in range(N):
    for j in range(M):
        if board[i][j] == 'I':
            sy,sx = i,j

def dfs(y,x):
    visit = [[False for _ in range(M)] for _ in range(N)]
    dir = [(0,1),(0,-1),(1,0),(-1,0)]
    stack = [(y,x)]
    visit[y][x] = True
    cnt = 0
    while stack:
        y,x = stack.pop()
        if board[y][x] == 'P':
            cnt += 1
        for d in dir:
            dy,dx = y+d[0], x+d[1]
            if 0 <= dy < N and 0 <= dx < M and not visit[dy][dx] and board[dy][dx] != 'X':
                visit[dy][dx] = True
                stack.append((dy,dx))

    return cnt

res = dfs(sy,sx)
print(res if res > 0 else "TT")
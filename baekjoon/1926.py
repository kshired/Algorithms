# https://acmicpc.net/problem/1926
# 그림

import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N,M = input_multiple_int()
board = []
visit = [[False for _ in range(M)] for _ in range(N)]
for _ in range(N):
    board.append(list(input_multiple_int()))

def bfs(y,x):
    q = deque()
    q.append((y,x))
    visit[y][x] = True
    dir = [(1,0),(0,1),(-1,0),(0,-1)]
    cnt = 0
    while q:
        y,x = q.popleft()
        cnt += 1
        for d in dir:
            dy,dx = y+d[0],x+d[1]
            if 0 <= dy < N and 0 <= dx < M and not visit[dy][dx]:
                if board[dy][dx] == 1:
                    visit[dy][dx] = True
                    q.append((dy,dx))
        if not q:
            return cnt

ans = 0
res = 0

for i in range(N):
    for j in range(M):
        if not visit[i][j] and board[i][j] == 1:
            ans += 1
            res = max(res,bfs(i,j))

print(ans)
print(res)






# https://acmicpc.net/problem/17836
# 공주님을 구해라!

import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N,M,T = input_multiple_int()
board = []
visit = [[-1 for _ in range(M)] for _ in range(N)]
dir = [(0,1),(0,-1),(1,0),(-1,0)]
res = T+1

for _ in range(N):
    board.append(list(input_multiple_int()))

def bfs(sy,sx):
    global res
    q = deque()
    q.append((sy,sx))
    visit[sy][sx] = 0

    while q:
        y,x = q.popleft()

        if board[y][x] == 2:
            res = abs(N-1-y) + abs(M-1-x) + visit[y][x]
        if y == N-1 and x == M-1:
            return min(res,visit[y][x])

        for d in dir:
            dy,dx = y+d[0],x+d[1]
            if 0 <= dy < N and 0 <= dx < M:
                if board[dy][dx] != 1 and visit[dy][dx] == -1:
                    visit[dy][dx] = visit[y][x] + 1
                    q.append((dy,dx))
    return res

ans = bfs(0,0)

if ans <= T:
    print(ans)
else:
    print("Fail")
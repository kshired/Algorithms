# https://acmicpc.net/problem/7562
# 나이트의 이동

import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())


def bfs(size,cur,target):
    board = [[0 for _ in range(size)] for _ in range(size)]
    dir = [(-1,-2),(-2,-1),(-2,1),(-1,2),(1,-2),(2,-1),(1,2),(2,1)]
    q = deque()

    q.append((cur[0],cur[1],0))
    board[cur[0]][cur[1]] = 1

    while q:
        y,x,cnt = q.popleft()
        if y == target[0] and x == target[1]:
            return cnt

        for i in dir:
            dy,dx = y+i[0], x+i[1]
            if 0<= dy < size and 0 <= dx < size and board[dy][dx] == 0:
                q.append((dy,dx,cnt+1))
                board[dy][dx] = 1

T = int(input())

for _ in range(T):
    N = int(input())
    cur_pos = tuple(input_multiple_int())
    target = tuple(input_multiple_int())
    print(bfs(N,cur_pos,target))

# https://acmicpc.net/problem/2206
# 벽 부수고 이동하기
'''
결국 혼자 힘으로 못 푼 문제.. ㅠㅠ

visit[y][x][0] => 벽을 아직 한 번도 안 부수고 지나온 최단 경로의 길이
visit[y][x][1] => 벽을 이미 한 번 부수고 지나온 최단 경로의 길이

약간 dp스럽게 bfs를 진행하는 느낌인데,
이런걸 처음 본 사람들은 도대체 어떻게 푸는건지ㅠ

더 노력합시다
'''

import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N,M = input_multiple_int()
board = []
dir = [(0,1),(0,-1),(1,0),(-1,0)]
visit = [[[-1,-1] for _ in range(M)] for _ in range(N)]

for _ in range(N):
    board.append(list(map(int,list(input()))))

def bfs(y,x,way):
    q = deque()
    q.append((y,x,way))
    visit[y][x][way] = 1

    while q:
        y,x,way = q.popleft()
        
        for d in dir:
            dy, dx = y + d[0], x + d[1]
            if 0 <= dy < N and 0 <= dx < M:
                if board[dy][dx] == 0 and visit[dy][dx][way] == -1:
                    visit[dy][dx][way] = visit[y][x][way] + 1
                    q.append((dy,dx,way))
                elif way == 0 and board[dy][dx] == 1 and visit[dy][dx][1] == -1:
                    visit[dy][dx][1] = visit[y][x][way] + 1
                    q.append((dy,dx,1))
        
bfs(0,0,0)

res1, res2 = visit[N-1][M-1]

if res1*res2 < 0:
    print(res1 if res1 != -1 else res2)
else:
    print(min(res1,res2))
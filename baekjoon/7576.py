# https://acmicpc.net/problem/7576
# 토마토

import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N, M = input_multiple_int()

dir = [(1,0),(-1,0),(0,1),(0,-1)]
tomato = []
q = deque()

for _ in range(M):
    tomato.append(list(input_multiple_int()))

for i in range(M):
    for j in range(N):
        if tomato[i][j] == 1:
            q.append((i,j))

res = 0
while q:
    res += 1
    for _ in range(len(q)):
        y,x = q.popleft()
        for i in range(4):
            ny,nx = y+dir[i][0], x+dir[i][1]
        
            if 0 <= ny < M  and 0 <= nx < N and tomato[ny][nx] == 0:
                tomato[ny][nx] = 1
                q.append((ny,nx))

for i in tomato:
    if 0 in i:
        print(-1)
        break
else:
    print(res)
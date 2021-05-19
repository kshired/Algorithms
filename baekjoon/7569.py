# https://acmicpc.net/problem/7569
# 토마토

import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N, M, H = input_multiple_int()

tomato = []
dir = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
q = deque()

for i in range(H):
    tomato.append([])
    for _ in range(M):
        tomato[i].append(list(input_multiple_int()))

for i in range(H):
    for j in range(M):
        for k in range(N):
            if tomato[i][j][k] == 1:
                q.append((i,j,k))

res = 0
while q:
    res += 1
    for _ in range(len(q)):
        z,y,x = q.popleft()
        for i in range(6):
            nz, ny, nx = z + dir[i][0], y + dir[i][1], x + dir[i][2]
            if 0 <= nz < H and 0 <= ny < M and 0 <= nx < N and tomato[nz][ny][nx] == 0:
                tomato[nz][ny][nx] = 1
                q.append((nz,ny,nx))

for i in tomato:
    for j in i:
        if 0 in j:
            print(-1)
            break
    else:
        continue
    break
else:
    print(res-1)
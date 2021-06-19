# https://acmicpc.net/problem/5014
# 스타트링크

import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

F,S,G,U,D = input_multiple_int()

q = deque()
visit = [-1 for _ in range(F+1)]
dir = [U,-D]

q.append(S)
visit[S] = 0

while q:
    now = q.popleft()
    if now == G:
        break
    
    for d in dir:
        next = now + d
        if 0 < next <= F and visit[next] == -1:
            visit[next] = visit[now] + 1
            q.append(next)

if visit[G] != -1:
    print(visit[G])
else:
    print("use the stairs")
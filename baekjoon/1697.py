# https://acmicpc.net/problem/1697
# 숨바꼭질

import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N, K = input_multiple_int()
q = deque()
q.append((N,0))
cnt = 0
visit = [False for _ in range(100001)]
while q:
    now, depth = q.popleft()
    if now == K:
        print(depth)
        break
    visit[now] = True
    next = [now+1,now-1,now*2]
    for i in next:
        if 0 <= i <= 100000 and not visit[i]:
            q.append((i,depth+1))

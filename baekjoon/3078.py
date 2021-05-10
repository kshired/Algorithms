# https://acmicpc.net/problem/3078
# 좋은 친구

import sys
from collections import deque

input = lambda : sys.stdin.readline().rstrip()

N, K = map(int,input().split())
cnt = 0
l = 0
h = 1
dq = [deque() for _ in range(21)]


for i in range(N):
    l = len(input())
    while True:
        if len(dq[l]) == 0:
            dq[l].append(i)
            break
        if i - dq[l][0] <= K:
            cnt += len(dq[l])
            dq[l].append(i)
            break
        else:
            dq[l].popleft()
            continue

print(cnt)
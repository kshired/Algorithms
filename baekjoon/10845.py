# https://acmicpc.net/problem/10845
# 큐

import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

q = deque()
N = int(input())

for _ in range(N):
    cmd = input()
    if cmd[:3] == 'pus':
        op,val = cmd.split()
        val = int(val)
        q.append(val)
    elif cmd[:3] == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif cmd[:3] == 'siz':
        print(len(q))
    elif cmd[:3] == 'emp':
        if q:
            print(0)
        else:
            print(1)
    elif cmd[:3] == 'fro':
        if q:
            print(q[0])
        else:
            print(-1)
    elif cmd[:3] == 'bac':
        if q:
            print(q[-1])
        else:
            print(-1)
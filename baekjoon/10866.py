# https://acmicpc.net/problem/10866
# 덱

import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

dq = deque()
N = int(input())

for _ in range(N):
    cmd = input()
    if cmd[:3] == 'pus':
        op,val = cmd.split()
        val = int(val)
        if op == 'push_front':
            dq.appendleft(val)
        elif op == 'push_back':
            dq.append(val)

    elif cmd[:3] == 'pop':
        if cmd == 'pop_front':
            if dq:
                print(dq.popleft())
            else:
                print(-1)
        elif cmd == 'pop_back':
            if dq:
                print(dq.pop())
            else:
                print(-1)
    elif cmd[:3] == 'siz':
        print(len(dq))
    elif cmd[:3] == 'emp':
        if dq:
            print(0)
        else:
            print(1)
    elif cmd[:3] == 'fro':
        if dq:
            print(dq[0])
        else:
            print(-1)
    elif cmd[:3] == 'bac':
        if dq:
            print(dq[-1])
        else:
            print(-1)
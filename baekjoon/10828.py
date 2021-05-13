# https://acmicpc.net/problem/10828
# 스택

import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

stack = deque()
N = int(input())

for _ in range(N):
    cmd = input()
    if cmd[:3] == 'pus':
        op,val = cmd.split()
        val = int(val)
        stack.append(val)
    elif cmd[:3] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif cmd[:3] == 'siz':
        print(len(stack))
    elif cmd[:3] == 'emp':
        if stack:
            print(0)
        else:
            print(1)
    elif cmd[:3] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
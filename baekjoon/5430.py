# https://acmicpc.net/problem/5430
# AC

import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

T = int(input())

for _ in range(T):
    cmd = input()
    n = int(input())
    if n == 0:
        input()
        arr = []
    else:
        arr = deque(map(int,input()[1:-1].split(',')))
    cnt = 0
    for i in cmd:
        if i == 'R':
            cnt += 1
        else:
            if arr:
                if cnt % 2:
                    arr.pop()
                else:
                    arr.popleft()
            else:
                print("error")
                break
    else:
        if cnt % 2:
            arr.reverse()
        res = ','.join(map(str,arr))
        print(f"[{res}]")
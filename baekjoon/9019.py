# https://acmicpc.net/problem/9019
# DSLR

import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N = int(input())

def change(cur,cmd):
    if cmd == 1:
        return (cur*2)%10000,'D'
    elif cmd == 2:
        if cur == 0:
            return 9999,'S'
        else:
            return cur-1,'S'
    elif cmd == 3:
        return int(cur%1000*10+cur//1000), 'L'
    elif cmd == 4:
        return int(cur%10*1000+cur//10), 'R'
        


def bfs(s,e):
    q = deque()
    q.append((s,''))
    visit = [False for _ in range(10000)]

    while q:
        now,cmds = q.popleft()

        for i in range(1,5):
            cur,cmd = change(now,i)
            if cur == e:
                return cmds+cmd
            if not visit[cur-1]:
                visit[cur-1] = True
                q.append((cur,cmds+cmd))
    

for _ in range(N):
    s,e = input_multiple_int()
    print(''.join(bfs(s,e)))
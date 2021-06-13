# https://acmicpc.net/problem/2479
# 경로 찾기

import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N,M = input_multiple_int()
node = []
for _ in range(N):
    node.append(input())

s,e = input_multiple_int()
visit = [False for _ in range(N)]

def check(s1,s2):
    cnt = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            cnt += 1
    if cnt == 1:
        return True
    else:
        return False
    
def bfs(s,e):
    q = deque()

    q.append(([s-1],s-1))
    visit[s-1] = True

    while q:
        path,v = q.popleft()

        if v == e-1:
            return path

        for idx,value in enumerate(node):
            if check(value,node[v]):
                if not visit[idx]:
                    q.append((path+[idx],idx))
                    visit[idx] = True

res = bfs(s,e)

if res is None:
    print(-1)

else:
    for i in res:
        print(i+1,end=' ')
    print()
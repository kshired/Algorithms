# https://acmicpc.net/problem/15650
# N과 M (2)

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N, M = input_multiple_int()
visit = [False for _ in range(N)]
res = []

def solve(depth):
    if depth == M:
        for i in res:
            print(i, end= ' ')
        print()
    
    for i in range(N):
        if not visit[i]:
            visit[i] = True
            if (res and res[-1] < i+1) or (len(res) == 0):
                res.append(i+1)
                solve(depth+1)
                res.pop()
            visit[i] = False

solve(0)
            
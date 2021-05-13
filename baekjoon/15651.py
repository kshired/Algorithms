# https://acmicpc.net/problem/15651
# N과 M (3)

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N, M = input_multiple_int()

res = []

def solve(depth):
    if depth == M:
        for i in res:
            print(i,end=' ')
        print()
        return
    
    for i in range(N):
        res.append(i+1)
        solve(depth+1)
        res.pop()

solve(0)
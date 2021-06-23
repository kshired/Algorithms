# https://acmicpc.net/problem/10942
# 팰린드롬?

import sys
sys.setrecursionlimit(10**7)
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N = int(input())
values = list(input_multiple_int())
dp = [[-1 for _ in range(N)] for _ in range(N)]

def solve(i,j):
    if dp[i][j] == -1:
        if i == j:
            dp[i][j] = 1
        elif j - i == 1:
            if values[i] == values[j]:
                dp[i][j] = 1
            else:
                dp[i][j] = 0
        else:
            if values[i] == values[j]:
                dp[i][j] = solve(i+1,j-1)
            else:
                dp[i][j] = 0
    return dp[i][j]

M = int(input())

for i in range(N):
    for j in range(i,N):
        solve(i,j)

for _ in range(M):
    s,e = input_multiple_int()
    print(dp[s-1][e-1])

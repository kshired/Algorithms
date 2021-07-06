# https://acmicpc.net/problem/11049
# 행렬 곱셈 순서

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N = int(input())
d = []
dp = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    first,last = input_multiple_int()
    if i == 0:
        d.append(first)
    d.append(last)

for l in range(1,N):
    for i in range(N-l):
        j = i + l
        dp[i][j] = 1e9+7
        for k in range(i,j):
            dp[i][j] = min(dp[i][k]+dp[k+1][j]+d[i-1]*d[k]*d[j],dp[i][j])

print(dp[0][N-1])
# https://acmicpc.net/problem/11051
# 이항 계수 2

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N,K = input_multiple_int()
MOD = 10007
dp = [[0 for _ in range(N+1)] for i in range(N+1)]
dp[0][0] = 1

for i in range(1,N+1):
    dp[i][0] = 1
    for j in range(1,i+1):
        dp[i][j] = (dp[i-1][j-1] + dp[i-1][j])%MOD

print(dp[N][K])

# https://acmicpc.net/problem/2225
# 합분해

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

MOD = int(1e+9)

N,K = input_multiple_int()

dp = [[1 for _ in range(K+1)] for _ in range(N+1)]

for i in range(1,K+1):
    dp[1][i] = i

for i in range(2,N+1):
    for j in range(2,K+1):
        dp[i][j] = (dp[i][j-1] + dp[i-1][j])%MOD
    
print(dp[N][K])

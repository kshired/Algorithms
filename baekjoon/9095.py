# https://acmicpc.net/problem/9095
# 1, 2, 3 더하기

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N = 10

dp = [0 for _ in range(N+1)]
dp[0] = 1
dp[1] = 1
dp[2] = 2 # 1+1 , 2

for i in range(3,N+1):
    dp[i] += dp[i-1]
    dp[i] += dp[i-2]
    dp[i] += dp[i-3]

T = int(input())
for _ in range(T):
    n = int(input())
    print(dp[n])
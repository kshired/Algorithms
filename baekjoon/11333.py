# https://acmicpc.net/problem/11333
# 4×n 타일링

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

MOD = int(1e9+7)
dp = [0 for _ in range(10001)]
T = int(input())
dp[0] = 1
dp[3] = 3
dp[6] = 13

for i in range(9,10001,3):
    dp[i] = (5*dp[i-3] - 3*dp[i-6] + dp[i-9])%MOD


for _ in range(T):
    print(dp[int(input())]%MOD)
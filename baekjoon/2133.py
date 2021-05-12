# https://acmicpc.net/problem/2133
# 타일 채우기

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N = int(input())

if N % 2:
    print(0)
else:
    dp = [0 for _ in range(N+1)]
    dp[0] = 1
    dp[2] = 3
    for i in range(4,N+1):
        if i % 2:
            continue
        dp[i] = dp[i-2]*3
        for j in range(i-4,-1,-2):
            dp[i] += dp[j]*2
    print(dp[N])
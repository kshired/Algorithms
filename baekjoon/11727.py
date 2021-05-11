# https://acmicpc.net/problem/11727
# 2×n 타일링 2

import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
mod = 10007
dp = [0 for _ in range(1001)]

dp[0] = 1
dp[1] = 1

'''
f(n) = 2f(n-2) + f(n-1)
'''

for i in range(2,n+1):
    dp[i] = (2*dp[i-2] + dp[i-1])%mod

print(dp[n])
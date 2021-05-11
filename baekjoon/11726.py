# https://acmicpc.net/problem/11726
# 2×n 타일링

'''
1 -> 1개
2 -> f(1) + 1x2 1개, f(0) + 2x1 두개 -> 1 + 1 -> 2
3 -> f(2) + 1x2 1개, f(1) + 2x1 두개 -> 1 + 2 -> 3
f(n) = f(n-1) + f(n-2)
'''

import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
mod = 10007
dp = [0 for _ in range(1001)]
dp[0] = 1
dp[1] = 1

for i in range(2,n+1):
    dp[i] = (dp[i-1] + dp[i-2])%mod

print(dp[n])
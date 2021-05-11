# https://acmicpc.net/problem/1699
# 제곱수의 합

import sys
input = lambda : sys.stdin.readline().rstrip()

MAX = 987654321
N = int(input())

dp = [0 for _ in range(N+1)]
square = [i**2 for i in range(1,317)]

for i in range(1,N+1):
    res = []
    for j in square:
        if j > i:
            break
        res.append(dp[i-j])
    dp[i] = min(res) + 1
print(dp[N])
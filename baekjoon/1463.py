# https://acmicpc.net/problem/1463
# 1로 만들기

import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
dp = [10**8 for _ in range(10**6+1)]
dp[1] = 0
for i in range(1,N):
    dp[i+1] = min(dp[i+1],dp[i] + 1)
    if i*3 <= N:
        dp[i*3] = min(dp[i*3],dp[i] + 1)
    if i*2 <= N:
        dp[i*2] = min(dp[i*2],dp[i] + 1)

print(dp[N])

# import sys
# sys.setrecursionlimit(10**7)

# N = int(input())
# dp = [-1 for _ in range(N+1)]
# dp[1] = 0

# def solve(n):
#     if dp[n] != -1:
#         return dp[n]
#     else:
#         dp[n] = solve(n-1) + 1
#         if n % 3 == 0:
#             dp[n] = min(dp[n], solve(n//3) + 1)
#         if n % 2 == 0:
#             dp[n] = min(dp[n], solve(n//2) + 1)
#         return dp[n]

# print(solve(N))
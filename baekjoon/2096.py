# https://acmicpc.net/problem/2096
# 내려가기

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N = int(input())
max_dp = [[0 for _ in range(3)] for _ in range(2)]
min_dp = [[0 for _ in range(3)] for _ in range(2)]

for i in range(N):
    max_dp[1][0] = max(max_dp[0][0],max_dp[0][1])
    min_dp[1][0] = min(min_dp[0][0],min_dp[0][1])

    max_dp[1][1] = max(max_dp[0][0],max(max_dp[0][1],max_dp[0][2]))
    min_dp[1][1] = min(min_dp[0][0],min(min_dp[0][1],min_dp[0][2]))

    max_dp[1][2] = max(max_dp[0][1],max_dp[0][2])
    min_dp[1][2] = min(min_dp[0][1],min_dp[0][2])

    for idx,val in enumerate(input_multiple_int()):
        max_dp[0][idx] = max_dp[1][idx] + val
        min_dp[0][idx] = min_dp[1][idx] + val

print(max(max_dp[0]),min(min_dp[0]))
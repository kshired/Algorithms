# https://acmicpc.net/problem/14728
# 벼락치기

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N, T = input_multiple_int()
cost = [0]
weight = [0]

for _ in range(N):
    w,c = input_multiple_int()
    cost.append(c)
    weight.append(w)

dp = [[0 for _ in range(T+1)] for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,T+1):
        if weight[i] <= j:
            dp[i][j] = max(dp[i-1][j-weight[i]] + cost[i], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[-1][-1])
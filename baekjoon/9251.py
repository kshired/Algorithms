# https://acmicpc.net/problem/9251
# LCS

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

s1 = '0'+input()
s2 = '0'+input()

N,M = len(s1), len(s2)

dp = [[0 for _ in range(N)] for _ in range(M)]

for i in range(1,M):
    for j in range(1,N):
        if s1[j] == s2[i]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
print(max(dp[M-1]))
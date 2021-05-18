# https://acmicpc.net/problem/1958
# LCS 3

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

s1 = '0'+input()
s2 = '0'+input()
s3 = '0'+input()
N,M,L = len(s1),len(s2),len(s3)


dp = [[[0 for _ in range(L)] for _ in range(N)] for _ in range(M)]

res = 0
for i in range(1,M):
    for j in range(1,N):
        for k in range(1,L):
            if s1[j] == s2[i] and s1[j] == s3[k]:
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1
            else:
                dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])
            res = max(res,dp[i][j][k])

print(res)
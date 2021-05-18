# https://acmicpc.net/problem/1915
# 가장 큰 정사각형

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N,M = input_multiple_int()
board = []

for _ in range(N):
    board.append(list(map(int,list(input()))))

dp = [[0 for _ in range(M)] for _ in range(N)]
for i in range(M):
    dp[0][i] = board[0][i]
for i in range(N):
    dp[i][0] = board[i][0]

for i in range(1,N):
    for j in range(1,M):
        if board[i][j] != 0:
            dp[i][j] = min(dp[i-1][j],min(dp[i][j-1],dp[i-1][j-1]))+1

maximum = 0
for i in dp:
    maximum = max(maximum,max(i))

print(maximum**2)
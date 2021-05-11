# https://acmicpc.net/problem/9465
# 스티커

'''
dp[i][j] = (i,j)까지 차례로 떼어서 가질 수 있는 스티커 점수합의 최댓값

현재 값 += max(1칸 전 대각선의 점수, 2칸 전 대각선의 점수)
'''

import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())

for _ in range(N):
    n = int(input())
    dp = []
    for __ in range(2):
        dp.append(list(map(int,input().split())))
    
    for i in range(1,n):
        if i >= 2:
            dp[0][i] += max(dp[1][i-2],dp[1][i-1])
            dp[1][i] += max(dp[0][i-2],dp[0][i-1])
        else:
            dp[0][i] += dp[1][i-1]
            dp[1][i] += dp[0][i-1]
    print(max(max(dp[0]),max(dp[1])))
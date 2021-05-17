# https://acmicpc.net/problem/13398
# 연속합 2

'''
dp[i][0] = 한 개를 제거하지 않고 i번째까지의 가장 큰 연속합
dp[i][1] = 한 개를 제거하고 i번째까지의 가장 큰 연속합

dp[i][0] = max(arr[i], dp[i-1][0]+arr[i])
dp[i][1] = max(dp[i-1][0],dp[i-1][1]+arr[i])
'''

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split()z)

n = int(input())
arr = list(input_multiple_int())
dp = [[arr[0],arr[0]]]

res = max(dp[0][0],dp[0][1])
for i in range(1,n):
    dp.append([max(arr[i], dp[i-1][0]+arr[i]),max(dp[i-1][0],dp[i-1][1]+arr[i])])
    res = max(res,max(dp[i]))

print(res)
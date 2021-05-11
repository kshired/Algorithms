# https://acmicpc.net/problem/11055
# 가장 큰 증가 부분 수열

import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
arr = list(map(int,input().split()))
dp = [0 for _ in range(N)]

for i in range(N):
    dp[i] = arr[i]

for i in range(1,N):
    for j in range(i-1,-1,-1):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + arr[i])
    
print(max(dp))
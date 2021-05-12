# https://acmicpc.net/problem/11054
# 가장 긴 바이토닉 부분 수열

import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
arr = list(map(int,input().split()))
dp1 = [1 for _ in range(N)]
dp2 = [1 for _ in range(N)]

for i in range(1,N):
    for j in range(i):
        if arr[j] < arr[i]:
            dp1[i] = max(dp1[i],dp1[j] + 1)

arr.reverse()

for i in range(1,N):
    for j in range(i):
        if arr[j] < arr[i]:
            dp2[i] = max(dp2[i],dp2[j] + 1)

dp2.reverse()

res = 0
for i in range(N):
    res = max(res,dp1[i]+dp2[i])

print(res-1)
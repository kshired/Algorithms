# https://acmicpc.net/problem/16194
# 카드 구매하기 2

"""
dp[i] = i개의 카드를 살 때 최소 값.

dp[i] = min(dp[i], dp[i-j] + dp[j])
"""


import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N = int(input())
cards = list(input_multiple_int())
dp = [0 for _ in range(N+1)]
dp[1] = cards[0]

for i in range(2,N+1):
    dp[i] = cards[i-1]
    for j in range(1,i):
        dp[i] = min(dp[i], dp[i-j] + dp[j])

print(dp[N])
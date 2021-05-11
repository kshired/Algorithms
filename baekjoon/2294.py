# https://acmicpc.net/problem/2294
# 동전 2
'''
dp[i] = i원을 만들 때 드는 동전의 최소 개수.
'''

import sys
sys.setrecursionlimit(10**6)
input = lambda : sys.stdin.readline().rstrip()

MAX = 987654321
n,k = map(int,input().split())
arr = [0 for _ in range(101)]

for i in range(n):
    arr[i] = int(input())

dp = [MAX for _ in range(100001)]

for i in arr[:n]:
    dp[i] = 1
dp[0] = 0

def solve(k):
    if dp[k] != MAX:
        return dp[k]

    res = MAX
    for i in arr[:n]:
        if k - i >= 0:
            res = min(res,solve(k-i) + 1)
    
    dp[k] = res

    if 0 <= dp[k] <= 10001:
        return dp[k]
    else:
        return 10002

res = solve(k)
if res > 10001:
    print(-1)
else:
    print(res)
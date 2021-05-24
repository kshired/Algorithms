# https://acmicpc.net/problem/7579
# 앱

'''
그냥 이름만 다른 0-1 knapsack 문제.

knapsack에서 사용하던,
"dp[i][w] = i물품까지 w의 무게로 얻을 수 있는 최대 가치"를 그대로 가져와서.

case1 ) val[i] <= w
dp[i][w] = max(arr[i]+dp[i-1][w-val[i]],dp[i-1][w])

case2 ) val[i] > w
dp[i][w] = dp[i-1][w]

위와 같이 case를 나눠준 후, dp[i][w] >= M을 만족하는 최소의 w를 구하면 된다.
'''

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N,M = input_multiple_int()
arr = [0] + list(input_multiple_int())
val = [0] + list(input_multiple_int())
dp = [[0 for _ in range(sum(val)+1)] for _ in range(N+1)]

for i in range(1,N+1):
    for w in range(1,sum(val)+1):
        if val[i] <= w:
            dp[i][w] = max(arr[i]+dp[i-1][w-val[i]],dp[i-1][w])
        else:
            dp[i][w] = dp[i-1][w]

res = [j for j in range(sum(val)+1) for i in range(N+1) if dp[i][j] >= M]
print(min(res))
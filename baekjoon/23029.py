# https://acmicpc.net/problem/23029
# 시식 코너는 나의 것

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N = int(input())
values = []

for _ in range(N):
    values.append(int(input()))

dp = [[0,0] for _ in range(N)]

if N == 1:
    print(values[0])
    exit()


# dp[n][0] => n번째로 먹는 음식이 연속이지 않은 경우
# dp[n][1] => n번째로 먹는 음식이 연속인 경우

dp[0][0] = values[0]
dp[0][1] = values[0]

dp[1][0] = max(values[1],values[0])
dp[1][1] = values[0] + values[1]//2

# 지금 안먹고 넘어가는 경우가 있음 => 포도주 시식인가 그 문제 생각남..
for i in range(2,N):
    dp[i][0] = max(dp[i-1][1],max(dp[i-2]) + values[i])
    dp[i][1] = dp[i-1][0] + values[i]//2

m = 0
for i in range(N):
    m = max(m,dp[i][0],dp[i][1])
print(m)
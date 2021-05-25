# https://acmicpc.net/problem/12852
# 1로 만들기 2

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N = int(input())
dp = [0 for _ in range(N+1)]
trace = [0 for _ in range(N+1)]

for i in range(2,N+1):
    dp[i] = dp[i-1] + 1
    trace[i] = i-1
    if i%2 == 0:
        if dp[i] > dp[i//2]+1:
            dp[i] = dp[i//2]+1
            trace[i] = i//2
    if i%3 == 0:
        if dp[i] > dp[i//3]+1:
            dp[i] = dp[i//3]+1
            trace[i] = i//3

chk = N
res = []
while chk != 0:
    res.append(chk)
    chk = trace[chk]

print(dp[N])
print(*res)
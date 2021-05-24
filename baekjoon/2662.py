# https://acmicpc.net/problem/2662
# 기업투자

'''
arr[i][j] : i 기업에 j원 투자 했을 때 얻는 가치
dp[i][j] : i까지의 기업에 j원을 투자하여 얻을 수 있는 최대 이익
path[i][j] : dp[i][j]를 구했을 때, i 기업에 투자하는 금액
'''

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N,M = input_multiple_int()

arr = [[0 for _ in range(N+1)] for _ in range(M+1)]
dp = [[0 for _ in range(N+1)] for _ in range(M+1)]
path = [[0 for _ in range(N+1)] for _ in range(M+1)]


for _ in range(N):
    values = list(input_multiple_int())
    for i in range(1,M+1):
        arr[i][values[0]] = values[i]

for i in range(1,M+1):
    for j in range(1,N+1):
        for k in range(j+1):
            tmp = dp[i-1][j-k] + arr[i][k]
            if tmp > dp[i][j]:
                dp[i][j] = tmp
                path[i][j] = k
        
print(dp[-1][-1])

ans = []
cur = M
cost = N

while cur > 0:
    now = path[cur][cost]
    ans.append(now)

    cost -= now
    cur -= 1

print(*reversed(ans))
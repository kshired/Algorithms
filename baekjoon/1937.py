# https://acmicpc.net/problem/1937
# 욕심쟁이 판다

import sys
sys.setrecursionlimit(10**6)
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N = int(input())
forest = []

for _ in range(N):
    forest.append(list(input_multiple_int()))

dir = [(0,1),(0,-1),(1,0),(-1,0)]
dp = [[0 for _ in range(N)] for _ in range(N)]

def dfs(y,x):
    if dp[y][x] == 0:
        dp[y][x] = 1
        
        for d in dir:
            dy,dx = y+d[0],x+d[1]
            if 0 <= dy < N and 0 <= dx < N:
                if forest[dy][dx] > forest[y][x]:
                    dp[y][x] = max(dp[y][x],dfs(dy,dx)+1)

    return dp[y][x]

res = 0
for i in range(N):
    for j in range(N):
        res = max(res,dfs(i,j))

print(res)
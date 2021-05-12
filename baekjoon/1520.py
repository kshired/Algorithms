# https://acmicpc.net/problem/1520
# 내리막 길

'''
dp를 이용한 dfs문제.

dp 배열을 아래와 같이 정의하고, 이미 계산했는지 여부를 체크하기위해 -1로 초기화.
dp[i][j] = (i,j) 부터 도착지점까지의 경로의 갯수

위와 같이 정의한 dp배열을 이용하여,
dfs 탐색을 진행하여 도착 지점에 도착하였다면 값을 +1 해준다.
'''

import sys
sys.setrecursionlimit(10**6)

input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N, M = input_multiple_int()
arr = []
for _ in range(N):
    arr.append(list(input_multiple_int()))
dp = [[-1 for _ in range(M)] for _ in range(N)]
dir = [(-1,0),(1,0),(0,-1),(0,1)]

def dfs(y,x):
    if y == N-1 and x == M-1:
        return 1
    
    if dp[y][x] == -1:
        dp[y][x] = 0
        for i in range(4):
            ny, nx = y + dir[i][0], x + dir[i][1]
            if (0 <= ny <= N-1) and (0 <= nx <= M-1) and arr[y][x] > arr[ny][nx]:
                dp[y][x] += dfs(ny,nx)

    return dp[y][x]

print(dfs(0,0))
    
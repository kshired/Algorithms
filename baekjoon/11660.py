# https://acmicpc.net/problem/11660
# 구간 합 구하기 5

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N,M = input_multiple_int()

arr = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(N):
    tmp = list(input_multiple_int())
    for j in range(len(tmp)):
        arr[i+1][j+1] = arr[i+1][j] + arr[i][j+1] - arr[i][j] + tmp[j]

for _ in range(M):
    x1,y1,x2,y2 = input_multiple_int()
    print(arr[x2][y2] - arr[x1-1][y2] - arr[x2][y1-1] + arr[x1-1][y1-1])  

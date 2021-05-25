# https://acmicpc.net/problem/2166
# 다각형의 면적

'''
그냥 고등학교 때 간간히 야매로 써먹었던
신발끈 공식을 썼다.
'''

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N = int(input())
arr = []

for _ in range(N):
    arr.append(list(input_multiple_int()))

res = 0
for i in range(N-1):
    res += arr[i][0]*arr[i+1][1]-arr[i+1][0]*arr[i][1]

res += arr[-1][0]*arr[0][1]-arr[0][0]*arr[-1][1]

print("%.1f"%(abs(res)/2))
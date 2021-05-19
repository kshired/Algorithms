# https://acmicpc.net/problem/14003
# 가장 긴 증가하는 부분 수열 5

import sys
from bisect import bisect_left
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N = int(input())

arr = list(input_multiple_int())
lis = []
trace = [0 for _ in range(N+1)]

def LIS(n):
    maxVal = 0

    for i in range(n):
        if i == 0 or lis[-1] < arr[i]:
            lis.append(arr[i])
            trace[i] = len(lis)-1
            maxVal = trace[i]
        else:
            pos = bisect_left(lis, arr[i])
            lis[pos] = arr[i]
            trace[i] = pos
    print(maxVal+1)

    res = []
    for i in range(n-1,-1,-1):
        if trace[i] == maxVal:
            res.append(arr[i])
            maxVal -= 1
    res.reverse()
    print(*res)

LIS(N)
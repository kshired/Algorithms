# https://acmicpc.net/problem/2550
# 전구

import sys
from collections import defaultdict
from bisect import bisect_left
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

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
            res.append(arr2[arr[i]])
            maxVal -= 1
    res.sort()
    print(*res)

N = int(input())
arr1 = list(input_multiple_int())
arr2 = list(input_multiple_int())
arr = []
trace = [0 for _ in range(N)]
d = defaultdict()

for i in range(N):
    d[arr2[i]] = i

for i in range(N):
    arr.append(d[arr1[i]])

lis = []
LIS(N)
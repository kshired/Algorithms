# https://acmicpc.net/problem/2568
# 전깃줄 - 2

import sys
from bisect import bisect_left
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

def LIS(n):
    maxVal = 0
    for i in range(n):
        if i == 0 or lis[-1] < arr[i][1]:
            lis.append(arr[i][1])
            trace[i] = len(lis)-1
            maxVal = trace[i]
        else:
            pos = bisect_left(lis, arr[i][1])
            lis[pos] = arr[i][1]
            trace[i] = pos
    print(n-maxVal-1)

    res = []
    for i in range(n-1,-1,-1):
        if trace[i] == maxVal:
            d[arr[i][0]] = 0
            maxVal -= 1
    return res


N = int(input())
arr = []
lis = []
d = dict()
trace = [-1 for _ in range(N)]
for _ in range(N):
    f,s = input_multiple_int()
    arr.append((f,s))
    d[f] = 1

arr.sort()

res = LIS(N)
ans = []
for i in d.keys():
    if d[i] == 1:
        ans.append(i)
ans.sort()
for i in ans:
    print(i)
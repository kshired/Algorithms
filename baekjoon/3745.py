# https://acmicpc.net/problem/3745
# 오름세

import sys
from bisect import bisect_left
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

def LIS(n):
    for i in range(n):
        if i == 0 or lis[-1] < arr[i]:
            lis.append(arr[i])
        else:
            pos = bisect_left(lis, arr[i])
            lis[pos] = arr[i]

    print(len(lis))

lines = sys.stdin.readlines()

for i in range(0,len(lines),2):
    N = int(lines[i])
    arr = list(map(int,lines[i+1].split()))
    lis = []
    LIS(N)
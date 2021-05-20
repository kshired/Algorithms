# https://acmicpc.net/problem/13711
# LCS 4

import sys
from collections import defaultdict
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

N = int(input())
arr1 = list(input_multiple_int())
arr2 = list(input_multiple_int())
arr = []
d = defaultdict()

for i in range(N):
    d[arr2[i]] = i

for i in range(N):
    arr.append(d[arr1[i]])

lis = []
LIS(N)
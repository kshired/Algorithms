# https://acmicpc.net/problem/12014
# 주식

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

    return len(lis)

T = int(input())
for i in range(T):
    N,K = input_multiple_int()
    arr = list(input_multiple_int())
    lis = []
    res = LIS(N)
    if res >= K:
        print(f"Case #{i+1}\n{1}")
    else:
        print(f"Case #{i+1}\n{0}")
# https://acmicpc.net/problem/11659
# 구간 합 구하기 4

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N,M = input_multiple_int()

arr = list(input_multiple_int())
prefix_sum = [arr[0]]
for i in range(1,len(arr)):
    prefix_sum.append(arr[i]+prefix_sum[i-1])

for _ in range(M):
    s,e = input_multiple_int()
    if s == 1:
        print(prefix_sum[e-1])
    else:
        print(prefix_sum[e-1]-prefix_sum[s-2])

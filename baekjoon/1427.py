# https://acmicpc.net/problem/1427
# 소트인사이드

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N = list(input())
N.sort(reverse=True)
res = int(''.join(N))

print(res)
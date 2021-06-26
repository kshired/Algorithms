# https://acmicpc.net/problem/1427
# 소트인사이드

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N = list(input())
res = int(''.join(N.sort(reverse=True)))

print(res)
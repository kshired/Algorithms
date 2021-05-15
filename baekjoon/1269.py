# https://acmicpc.net/problem/1269
# 대칭 차집합

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())


N,M = input_multiple_int()
setA = set(input_multiple_int())
setB = set(input_multiple_int())
print(N+M-len(setA.intersection(setB))*2)

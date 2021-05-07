# https://acmicpc.net/problem/1037
# 약수

import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
divisor = list(map(int,input().split()))
divisor.sort()

print(divisor[0]*divisor[-1])
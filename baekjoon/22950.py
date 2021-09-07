# https://acmicpc.net/problem
# 이진수 나눗셈

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N = int(input())
M = int(input(),2)
K = 2**int(input())


print("YES" if M%K == 0 else "NO")
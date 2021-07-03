# https://acmicpc.net/problem/9656
# 돌 게임 2

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

ans = ['SK','CY']

print(ans[int(input())%2])
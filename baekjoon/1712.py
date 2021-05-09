# https://acmicpc.net/problem/1712
# 손익분기점

import sys
input = lambda : sys.stdin.readline().rstrip()

a,b,c = map(int, input().split())
if b >= c:
    print(-1)
else:
    print(a//(c-b)+1)
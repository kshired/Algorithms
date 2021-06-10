# https://acmicpc.net/problem/21868
# 미적분학 입문하기

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

e1,e2 = input_multiple_int()
x,c = input_multiple_int()
x0 = int(input())

res1 = x*x0 + c
res2 = e1
res3 = x*e2

print(res1)

if x == 0:
    print(0,0)
else:
    
    print(abs(res2),abs(res3))
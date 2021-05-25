# https://acmicpc.net/problem/17387
# 선분 교차 2

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

def ccw(a,b,c):
    op = a[0]*b[1] + b[0]*c[1] + c[0]*a[1]
    op -= (a[1]*b[0] + b[1]*c[0] + c[1]*a[0])
    if op > 0:
        return 1
    elif op == 0:
        return 0
    else:
        return -1

def isIntersect(x,y):
    a = x[0]
    b = x[1]
    c = y[0]
    d = y[1]
    ab = ccw(a,b,c)*ccw(a,b,d)
    cd = ccw(c,d,a)*ccw(c,d,b)
    if ab ==0 and cd == 0:
        if a > b:
            a,b = b,a
        if c > d:
            c,d = d,c
        return c <= b and a <= d
    return ab <= 0 and cd <= 0


x = list(input_multiple_int())
y = list(input_multiple_int())

if isIntersect((x[:2],x[2:]),(y[:2],y[2:])):
    print(1)
else:
    print(0)
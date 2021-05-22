# https://acmicpc.net/problem/12781
# PIZZA ALVOLOC

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
    if ccw(x[0],x[1],y[0])*ccw(x[0],x[1],y[1]) == -1:
        return True
    return False


x1,y1,x2,y2,x3,y3,x4,y4 = input_multiple_int()

if isIntersect(((x1,y1),(x2,y2)),((x3,y3),(x4,y4))):
    print(1)
else:
    print(0)
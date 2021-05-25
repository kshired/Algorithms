# https://acmicpc.net/problem/11758
# CCW

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


a = list(input_multiple_int())
b = list(input_multiple_int())
c = list(input_multiple_int())

print(ccw(a,b,c))
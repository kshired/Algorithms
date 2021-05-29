# https://acmicpc.net/problem/1708
# 볼록 껍질

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

def get_degree(p1,p2):
    return p2[0]-p1[0], p2[1]-p1[1]

def ccw(p1,p2,p3):
    u,v = get_degree(p1,p2), get_degree(p2,p3)
    if u[0] * v[1] > u[1] * v[0]:
        return True
    return False

def convex_hull(pos):
    convex = []
    for p3 in pos:
        while len(convex) >= 2:
            p1, p2 = convex[-2], convex[-1]
            if ccw(p1,p2,p3):
                break
            convex.pop()
        convex.append(p3)
    return len(convex)

N = int(input())
pos = []

for _ in range(N):
    pos.append(list(input_multiple_int()))

pos.sort(key=lambda x:(x[0],x[1]))
res = -2
res += convex_hull(pos)

pos.reverse()
res += convex_hull(pos)

print(res)
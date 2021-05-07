# https://acmicpc.net/problem/9012
# 괄호

import sys

input = lambda : sys.stdin.readline().rstrip()

N = int(input())

for _ in range(N):
    s = []
    for i in input():
        flag = False
        if i == '(':
            s.append(i)
        else:
            if len(s) == 0:
                print("NO")
                flag = True
                break
            if s[-1] == '(':
                s.pop()
            else:
                print("NO")
                break
    if s:
        print("NO")
    elif len(s) == 0 and not flag:
        print("YES")
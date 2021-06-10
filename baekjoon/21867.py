# https://acmicpc.net/problem/21867
# Java Bitecode

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

delete = ['J','A','V']

res = []
N = input()
for i in input():
    if i not in delete:
        res.append(i)

if res:
    print(''.join(res))
else:
    print('nojava')
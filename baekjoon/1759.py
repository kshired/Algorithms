# https://acmicpc.net/problem/1759
# 암호 만들기

import sys
from itertools import combinations
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

L,C = input_multiple_int()
values = input().split()
values.sort()

combis = combinations(values,L)

for combi in combis:
    cnt = 0
    for alpha in combi:
        if alpha in 'aeiou':
            cnt += 1

    if 1 <= cnt <= L-2:
        print(''.join(combi))
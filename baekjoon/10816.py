# https://acmicpc.net/problem/10816
# 숫자 카드 2

'''
해시 set(파이썬 dictionary)을 이용해 구현하면, 접근 할 때 O(1)이 걸림
'''

import sys
from collections import defaultdict

input = lambda : sys.stdin.readline().rstrip()
N = int(input())
values = defaultdict(int)


for i in map(int,input().split()):
    values[i] += 1

M = int(input())

for i in map(int,input().split()):
    print(values[i], end=' ')
print()
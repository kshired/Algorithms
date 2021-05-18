# https://acmicpc.net/problem/2812
# 크게 만들기

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N, K = input_multiple_int()
s = []
val = input()

for i in val:
    while K and s and s[-1] < int(i):
        s.pop()
        K -= 1
    s.append(int(i))

if K > 0:
    for i in range(K):
        s.pop()
print(''.join(map(str,s)))

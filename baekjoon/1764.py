# https://acmicpc.net/problem/1764
# 듣보잡

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N,M = input_multiple_int()
s1 = set()
s2 = set()

for _ in range(N):
    s1.add(input())

for _ in range(M):
    s2.add(input())

res = list(s1.intersection(s2))
res.sort()

print(len(res))
for i in res:
    print(i)
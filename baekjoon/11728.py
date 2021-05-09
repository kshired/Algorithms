# https://acmicpc.net/problem/11728
# 배열 합치기

import sys
input = lambda : sys.stdin.readline().rstrip()

n,m = map(int,input().split())
res = []

for i in map(int,input().split()):
    res.append(i)
for i in map(int,input().split()):
    res.append(i)

res.sort()

for i in res:
    print(i, end=' ')
print()
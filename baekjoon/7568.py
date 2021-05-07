# https://acmicpc.net/problem/7568
# 덩치

import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())

values = []
for _ in range(N):
    values.append(list(map(int,input().split())))

cnt = [0 for _ in range(N)]

for i in range(N):
    for j in range(N):
        if values[i][0] < values[j][0] and values[i][1] < values[j][1]:
            cnt[i] += 1

for i in cnt:
    print(i+1, end = ' ')
print()
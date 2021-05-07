# https://acmicpc.net/problem/1436
# 영화감독 숌

import sys
input = lambda : sys.stdin.readline().rstrip()

cnt = 0
i = 665

N = int(input())
while True:
    if cnt == N:
        break
    if str(i).count('666') >= 1:
        cnt += 1
    i += 1

print(i-1)
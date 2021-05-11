# https://acmicpc.net/problem/11047
# 동전 0

import sys
input = lambda : sys.stdin.readline().rstrip()

N, K = map(int, input().split())
arr = []
cnt = 0

for _ in range(N):
    arr.append(int(input()))

for i in arr[::-1]:
    if i <= K:
        cnt += K // i
        K = K % i

print(cnt)
# https://acmicpc.net/problem/1654
# 랜선 자르기

import sys
input = lambda : sys.stdin.readline().rstrip()

count = lambda cables, mid : sum([cable // mid for cable in cables if cable // mid])

def binary_search(cables, left, right, find):
    global res
    if left > right:
        return
    mid = (left + right)//2
    result = count(cables,mid)
    if result >= find:
        res = max(res, mid)
        binary_search(cables, mid+1, right, find)
    else:
        binary_search(cables, left, mid-1, find)

K, N = map(int,input().split())
cables = []
res = 0

for _ in range(K):
    cables.append(int(input()))

binary_search(cables, 1, max(cables), N)

print(res)
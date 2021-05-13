# https://acmicpc.net/problem/20301
# 반전 요세푸스

import sys
from collections import deque

input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N,K,M = input_multiple_int()

arr = deque([i for i in range(1,N+1)])

cnt = 0
flag = True

while arr:
    for i in range(K):
        if not arr:
            break
        if flag:
            val = arr.popleft()
            if i == K-1 or not arr:
                print(val)
            else:
                arr.append(val)
        else:
            val = arr.pop()
            if i == K-1 or not arr:
                print(val)
            else:
                arr.appendleft(val)

    cnt += 1   
    if cnt % M == 0:
        flag = not flag 
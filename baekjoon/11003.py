# https://acmicpc.net/problem/11003
# 최솟값 찾기

import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

N, L = map(int,input().split())
arr = list(map(int,input().split()))
dq = deque()

'''
arr[i-L+1 ~ i]
min
'''

for i in range(N):
    while dq and dq[-1][1] > arr[i]:
        dq.pop()
    
    dq.append((i,arr[i]))

    while dq and dq[0][0] < i - L + 1:
        dq.popleft()
    
    print(dq[0][1], end = ' ')
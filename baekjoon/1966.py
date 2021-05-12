# https://acmicpc.net/problem/1966
# 프린터 큐

import sys
from collections import deque

input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

def solution(priorities, location):
    s = deque()

    for idx,val in enumerate(priorities):
        s.append((val,idx))
    
    cnt = 1
    while s:
        val,idx = s.popleft()
        flag = True
        for i in s:
            if i[0] > val:
                s.append((val,idx))
                flag = False
                break
            
        if idx == location and flag:
            return cnt
        if flag:
            cnt += 1

T = int(input())

for _ in range(T):
    N,M = input_multiple_int()
    arr = list(input_multiple_int())
    print(solution(arr,M))
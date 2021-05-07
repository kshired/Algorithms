# https://acmicpc.net/problem/2805
# 나무 자르기

import sys

input = lambda : sys.stdin.readline().rstrip()

count = lambda values,mid: sum([value-mid for value in values if value-mid > 0 ]) 

def binary_search(values, left, right, find):
    global res
    if left > right:
        return
    mid = (left+right)//2
    result = count(values, mid)
    if result < find:
        binary_search(values, left, mid-1, find)
    elif result >= find:
        res = max(res,mid)
        binary_search(values, mid+1, right, find)
        

N, M = map(int,input().split())
values = list(map(int,input().split()))
res = 0

binary_search(values,0,max(values),M)
print(res)
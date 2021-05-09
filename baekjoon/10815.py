# https://acmicpc.net/problem/10815
# 숫자 카드

import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
values = list(map(int,input().split()))
values.sort()
M = int(input())

def binary_search(values, left, right, find):
    if left > right:
        return False
    mid = (left + right)//2
    if values[mid] == find:
        return True
    elif values[mid] > find:
        return binary_search(values, left, mid-1, find)
    else:
        return binary_search(values, mid+1, right, find)


for i in input().split():
    if binary_search(values, 0, len(values)-1, int(i)):
        print(1,end=' ')
    else:
        print(0,end=' ')
print()
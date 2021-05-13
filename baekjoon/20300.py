# https://acmicpc.net/problem/20300
# 서강근육맨

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N = int(input())
arr = list(input_multiple_int())
arr.sort()

if len(arr) % 2:
    minimum = arr[-1]
    for i in range((len(arr)-1)//2):
        minimum = max(minimum,arr[i]+arr[len(arr)-2-i])
else:
    minimum = 0
    for i in range((len(arr)//2)):
        minimum = max(minimum,arr[i]+arr[len(arr)-1-i])

print(minimum)
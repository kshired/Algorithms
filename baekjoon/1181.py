# https://acmicpc.net/problem/1181
# 단어 정렬

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

n = int(input())
arr = []
for _ in range(n):
    arr.append(input())

arr = list(set(arr))
arr.sort()
arr.sort(key=lambda x:len(x))

for i in arr:
    print(i)
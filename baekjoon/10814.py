# https://acmicpc.net/problem/10814
# 나이순 정렬

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N = int(input())
arr = []
for _ in range(N):
    age,name = input().split()
    arr.append([int(age),name])

arr.sort(key=lambda x:x[0])

for i in arr:
    print(i[0],i[1])
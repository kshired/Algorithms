# https://acmicpc.net/problem/10808
# 알파벳 개수

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

arr = [0 for _ in range(26)]

for i in input():
    arr[ord(i)-ord('a')] += 1

for i in arr:
    print(i, end=' ')
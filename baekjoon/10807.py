# https://acmicpc.net/problem/10807
# 개수 세기

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

n = input()
arr = [0 for _ in range(202)]

for i in input_multiple_int():
    arr[i+100] += 1

target = int(input())

print(arr[target+100])
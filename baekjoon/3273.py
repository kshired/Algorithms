# https://acmicpc.net/problem/3273
# 두 수의 합

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

n = int(input())
arr = list(input_multiple_int())
target = int(input())
check = [0 for _ in range(2000001)]

for i in arr:
    check[i] += 1


res = 0
for i in range(1,(target+1)//2):
    if check[i] == 1 and check[target-i] == 1:
        res += 1

print(res)
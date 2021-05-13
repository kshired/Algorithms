# https://acmicpc.net/problem/20302
# 민트 초코

import sys
from math import sqrt
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())
cnt = [0 for _ in range(100001)]

def chk(val, op):
    sqrt_val = int(sqrt(val))
    for i in range(2,sqrt_val+1):
        while val % i == 0:
            val //= i
            if op =='*':
                cnt[i] += 1
            else:
                cnt[i] -= 1
    if val > 1:
        if op =='*':
            cnt[val] += 1
        else:
            cnt[val] -= 1


n = int(input())

val = input().split()

if int(val) == 0:
    print('mint chocolate')
    sys.exit(0)

chk(abs(int(val[0])),'*')

for idx in range(1,len(val),2):
    value = abs(int(val[idx+1]))
    if value == 0:
        print('mint chocolate')
        sys.exit(0)
    chk(value,val[idx])

for i in cnt:
    if i < 0:
        print('toothpaste')
        sys.exit()

print('mint chocolate')
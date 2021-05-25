# https://acmicpc.net/problem/1208
# 부분수열의 합 2

'''
배열을 절반으로 나누어서,
부분 수열의 합을 left와 right dictionary에 count해줌.
그 후 이분 탐색을 이용해 경우의 수를 counting.
'''
import sys
from itertools import combinations
from collections import defaultdict
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N,S = input_multiple_int()
arr = list(input_multiple_int())

left = defaultdict(int)
right = defaultdict(int)

for i in range(N//2+1):
    tmp = combinations(arr[:N//2],i)
    for values in tmp:
        left[sum(values)] += 1

for i in range(N-N//2+1):
    tmp = combinations(arr[N//2:],i)
    for values in tmp:
        right[sum(values)] += 1

lkeys = sorted(left.keys())
rkeys = sorted(right.keys())
res = 0
l = 0
r = len(right)-1

while l < len(left) and r >= 0:
    tmp = lkeys[l] + rkeys[r]
    if tmp == S:
        res += left[lkeys[l]]*right[rkeys[r]]
        l += 1
        r -= 1
    elif tmp > S:
        r -= 1
    else:
        l += 1

if S == 0:
    res -= 1

print(res)
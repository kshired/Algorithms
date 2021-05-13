# https://acmicpc.net/problem/11866
# 요세푸스 문제 0

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N,K = input_multiple_int()

arr = [i for i in range(1,N+1)]
res = []
while arr:
    for i in range(K):
        arr.append(arr.pop(0))
    res.append(arr.pop())

print(f"<{', '.join(map(str,res))}>")
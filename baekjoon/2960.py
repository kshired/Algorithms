# https://acmicpc.net/problem/2960
# 에라토스테네스의 체

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N, K = input_multiple_int()

cnt = 0
isPrime = [True for _ in range(N+1)]

for i in range(2,N+1):
    if not isPrime[i]:
        continue
    cnt += 1
    isPrime[i] = False
    if cnt == K:
        print(i)
        break
    for j in range(i*2,N+1,i):
        if not isPrime[j]:
            continue
        isPrime[j] = False
        cnt += 1
        if cnt == K:
            print(j)
            break
    else:
        continue
    break
    

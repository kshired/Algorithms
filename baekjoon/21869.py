# https://acmicpc.net/problem/21869
# Maximum Bishop

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())


N = int(input())

if N == 1:
    print(1)
    print(1,1)
else:
    print((N-1)*2)
    for i in range(2,N+1):
        print(1,i)
    for i in range(2,N+1):
        print(N,i)
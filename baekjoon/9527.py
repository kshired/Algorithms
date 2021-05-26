# https://acmicpc.net/problem/9527
# 1의 개수 세기

'''
cntOne(x) => 1~x까지의 1의 개수, n은 x의 비트수.

x를 11001로 가정.
count 방법.
1. 1~1111까지 셈. => 1 ~ 2^N까지의 1의 개수 => N*2^(N-1) => (n-1)*2**(n-2)
2. 10000 ~ 11001 까지 수를 두 가지 방법으로 나눈 후 합쳐서 계산.
2-1. 10000 ~ 11001의 최상위 1의 개수는 0부터 1001까지 => x-2**(n-1)+1
2-2. 1001까지의 비트 수는 재귀를 통해 계산. => cntOne(x-2**(n-1))

-> 위의 것을 다 합치면 정답.
'''

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

def cntOne(x):
    if x == 0:
        return 0
    l = len(str(bin(x))) - 2
    high = x-2**(l-1)+1
    full = (l-1)*2**(l-2)
    remain = cntOne(x-2**(l-1))
    return int(high+full+remain)


A,B = input_multiple_int()

print(cntOne(B)-cntOne(A-1))
# https://acmicpc.net/problem/1919
# 애너그램 만들기

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

def solve(s1,s2):
    chk = [[0,0] for _ in range(26)]
    
    for i in s1:
        chk[ord(i)-ord('a')][0] += 1

    for i in s2:
        chk[ord(i)-ord('a')][1] += 1

    res = 0
    
    for i,j in chk:
        res += abs(i-j)
    
    return res

s1 = input()
s2 = input()

print(solve(s1,s2))
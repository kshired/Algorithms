# https://acmicpc.net/problem/11328
# Strfry

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

def solve(s1,s2):
    chk = [[0,0] for _ in range(26)]
    
    for i in s1:
        chk[ord(i)-ord('a')][0] += 1

    for i in s2:
        chk[ord(i)-ord('a')][1] += 1

    for i,j in chk:
        if i != j:
            return False
    
    return True


n = int(input())

for _ in range(n):
    s1, s2 = input().split()
    if solve(s1,s2):
        print("Possible")
    else:
        print("Impossible")
# https://acmicpc.net/problem/1182
# 부분수열의 합

import sys
sys.setrecursionlimit(10**7)
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N,S = input_multiple_int()
values = list(input_multiple_int())
res = 0

def solve(cnt,sum):
    global res
    if cnt == N:
        return
    if sum + values[cnt] == S:
        res += 1
    
    solve(cnt+1,sum)
    solve(cnt+1,sum+values[cnt])


solve(0,0)

print(res)
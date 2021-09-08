# https://acmicpc.net/problem
# 눈덩이 굴리기

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N,M = input_multiple_int()
snows = [0] + list(input_multiple_int())
ans = 0

def solve(res, idx, cnt):
    global ans
    if idx == N or cnt == 0:
        ans = max(ans,res)
        return
    
    if idx + 1 <= N:
        solve(res+snows[idx+1],idx+1,cnt-1)
    if idx + 2 <= N:
        solve(res//2+snows[idx+2],idx+2,cnt-1)
    
solve(1,0,M)
print(ans)
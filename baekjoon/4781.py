# https://acmicpc.net/problem/4781
# 사탕 가게

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

def convert(inp):
    n,m = inp.split()
    n = int(n)
    m = int(''.join(m.split('.')))
    return n,m

while True:
    inp = input()
    if inp == "0 0.00":
        break
    n,m = convert(inp)
    dp = [0 for _ in range(m+1)]
    for _ in range(n):
        c,w = convert(input())
        for i in range(w,m+1):
            dp[i] = max(dp[i],dp[i-w]+c)
    
    print(dp[m])
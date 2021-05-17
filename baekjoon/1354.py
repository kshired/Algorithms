# https://acmicpc.net/problem/1354
# 무한 수열 2

from collections import defaultdict
import sys
sys.setrecursionlimit(10**7)
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

dp = defaultdict(int)

N,P,Q,X,Y = input_multiple_int()

def solve(n):
    if n <= 0:
        return 1
    if dp[n] == 0:
        dp[n] = solve(n//P-X) + solve(n//Q-Y)
        return dp[n]
    else:
        return dp[n]
    
print(solve(N))
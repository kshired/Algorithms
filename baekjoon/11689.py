# https://acmicpc.net/problem/11689
# GCD(n, k) = 1

'''
oiler_phi(n) = n pi_{p|n}(1-1/p)
그대로 구현
'''
import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

n = int(input())

def oiler_phi(n):
    res = n
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            while n % i == 0:
                n //= i
            res *= 1-(1/i)
    if n > 1:
        res *= 1-(1/n)
    
    return int(res)

print(oiler_phi(n))
# https://acmicpc.net/problem/11729
# 하노이 탑 이동 순서

'''

n-1 개의 원판을 1 -> 2
n 번째 원판을 1 -> 3
n-1 개의 원판을 2 -> 3

'''

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

cnt = 0
res = []
def solve(n, a, b):
    global cnt, res
    if n == 1:
        cnt += 1
        res.append((a,b))
        return
    solve(n-1, a, 6-a-b)
    cnt += 1
    res.append((a,b))
    solve(n-1, 6-a-b, b)

n = int(input())
    
solve(n, 1, 3)

print(cnt)
for a,b in res:
    print(a,b)
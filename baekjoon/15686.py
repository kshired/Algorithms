# https://acmicpc.net/problem/15686
# 치킨 배달

import sys
from itertools import combinations
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N,M = input_multiple_int()
board = []

for _ in range(N):
    board.append(list(input_multiple_int()))

chicken = []
house = []

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            house.append((i+1,j+1))
        elif board[i][j] == 2:
            chicken.append((i+1,j+1))
        
    
def chicken_distance(chicken,house):
    res = 0
    for h in house:
        r = 1e9+7
        for c in chicken:
            r = min(r,abs(h[0]-c[0]) + abs(h[1]-c[1]))
        res += r
    return res

res = []
for i in range(1,M+1):
    chicken_combi = combinations(chicken,i)
    for ch in chicken_combi:
        res.append(chicken_distance(ch,house))

print(min(res))
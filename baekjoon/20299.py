# https://acmicpc.net/problem/20299
# 3대 측정

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N,K,L = input_multiple_int()
teams = []
for _ in range(N):
    teams.append(list(input_multiple_int()))

res = []

for team in teams:
    if sum(team) >= K:
        cnt = 0
        for member in team:
            if member >= L:
                cnt += 1
        if cnt == 3:
            res.append(team)

print(len(res))
for i in res:
    for member in i:
        print(member, end=' ')
print()

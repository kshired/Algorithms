# https://acmicpc.net/problem/13604
# Jogo de Estratégia

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

J,R = input_multiple_int()

values = list(input_multiple_int())
scores = [0 for _ in range(J)]

if J == 1:
    print(1)
    sys.exit()

for i in range(R):
    cnt = 0
    for j in range(J):
        scores[cnt] += values[j+i*J]
        cnt += 1


res = -1
max_value = max(scores)
for idx,value in enumerate(scores):
    if value == max_value:
        res = idx+1

print(res)
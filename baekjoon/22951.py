# https://acmicpc.net/problem
# 송이의 카드 게임

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N,K = input_multiple_int()
cards = []

for i in range(N):
    values = list(input_multiple_int())

    for value in values:
        cards.append([value,i+1])

idx = 0
length = N*K
while length > 1:
    length -= 1
    cnt = cards[idx][0]
    cards[idx][0] = -1
    
    while cnt > 0:
        if 0 <= idx+1 < N*K:
            idx += 1
        else:
            idx = 0
        if cards[idx][0] != -1:
            cnt -= 1

for value, people in cards:
    if value != -1:
        print(people,value)
        break

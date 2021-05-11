# https://acmicpc.net/problem/13904
# 과제

'''
가장 점수가 큰 과제부터 보면서,
그 과제를 가능한 날짜중 최대한 제일 늦게 배치하고,
가능한 날짜가 없으면 포기.
'''

import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())

arr = []

for _ in range(N):
    d,w = map(int,input().split())
    arr.append((d,w))

arr.sort(key=lambda x:(x[1]),reverse=True)
d = [0 for _ in range(1001)]


for i in arr:
    for j in range(i[0],0,-1):
        if d[j] == 0:
            d[j] = i[1]
            break
    
print(sum(d))
# https://acmicpc.net/problem/1931
# 회의실 배정

import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
arr = []

for _ in range(N):
    s,e = map(int,input().split())
    arr.append((s,e))

arr.sort(key=lambda x:x[0])
arr.sort(key=lambda x:x[1])

'''
시작 시간과 끝나는 시간이 같을 수 있기 때문에 시작시간을 기준으로 먼저 정렬
'''

cnt = 0
last = 0
for i in arr:
    if last <= i[0]:
        cnt += 1
        last = i[1]
print(cnt)
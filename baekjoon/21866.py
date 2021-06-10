# https://acmicpc.net/problem/21866
# 추첨을 통해 커피를 받자

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

arr = list(input_multiple_int())

chk = False
chkArr = [100,100,200,200,300,300,400,400,500]

for idx,val in enumerate(arr):
    if val > chkArr[idx]:
        chk = True
        break

if chk:
    print("hacker")
else:
    print('draw' if sum(arr) >= 100 else 'none')
    
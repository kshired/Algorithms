# https://www.acmicpc.net/problem/4344
# 평균은 넘겠지

import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
for _ in range(N):
    values = list(map(int,input().split()))
    cnt = 0
    avg = sum(values[1:])/len(values[1:])
    for i in values[1:]:
        if i > avg:
            cnt += 1
    print("%.3f%%"%(cnt*100/len(values[1:])))
# https://acmicpc.net/problem/17298
# 오큰수

'''
monotone stack을 이용하는 문제,
1. arr의 역순으로 스택에 넣으면서, 스택이 내림차순을 유지하도록 한다.
2. 자연스럽게 스택의 top은 arr[i]의 오큰수가 된다.
3. INF는 -1 값을 처리하는 용도
'''

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())


N = int(input())

arr = list(input_multiple_int())
s = [1e9+7]
ans = [0 for _ in range(N)]
for i in range(N-1,-1,-1):
    while s[-1] <= arr[i]:
        s.pop()
    if s[-1] >= 1e9:
        ans[i] = -1
    else:
        ans[i] = s[-1]
    s.append(arr[i])

for i in ans:
    print(i,end=' ')
print()
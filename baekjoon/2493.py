# https://acmicpc.net/problem/2493
# 탑

'''
1. arr를 거꾸로 stack에 삽입
2. 현재 arr[i]보다 큰 값 나올 때 까지, stack을 pop
3. stack을 pop하면서 res에 현재 arr index 기록
'''
import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N = int(input())
arr = list(input_multiple_int())
res = [0 for _ in range(N)]
s = []

for i in range(N-1,-1,-1):
    while s:
        if s[-1][0] < arr[i]:
            val,idx = s.pop()
            res[idx] = i+1
        else:
            break
    s.append((arr[i],i))

print(*res)
    

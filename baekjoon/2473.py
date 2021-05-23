# https://acmicpc.net/problem/2473
# 세 용액

'''
two pointers && binary search

정렬하고 차례로 한 idx를 잡아서
idx+1 ~ len(arr)-1 까지 이분 탐색을 하며 갱신.
'''


import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N = int(input())
arr = list(input_multiple_int())
arr.sort()

cmp = 1e10
res = []
for i in range(N-2):
    s = i + 1
    e = N - 1

    while s < e:
        val = arr[i] + arr[s] + arr[e]
        if abs(val) < abs(cmp):
            res = [arr[i],arr[s],arr[e]]
            cmp = val
        if val < 0:
            s += 1
        elif val > 0:
            e -= 1
        else:
            break
    else:
        continue
    break

for i in res:
    print(i,end=' ')
print()
# https://acmicpc.net/problem/10972
# 다음 순열

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

def next_permutation(arr):
	i = -1
	for idx in range(len(arr)-1):
		if arr[idx] < arr[idx+1]:
			i = max(i,idx)
	
	if i == -1:
		return -1

	j = i + 1
	for idx in range(i+1,len(arr)):
		if arr[idx] > arr[i]:
			j = max(idx,j)

	arr[i], arr[j] = arr[j], arr[i]

	arr[i+1:] = arr[len(arr):i:-1]

	return arr

N = int(input())
arr = list(input_multiple_int())

res = next_permutation(arr)

if res == -1:
    print(-1)
else:
    for i in res:
        print(i, end=' ')
    print()
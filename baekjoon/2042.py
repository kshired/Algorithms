# https://acmicpc.net/problem/2042
# 구간 합 구하기

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

def init(arr, tree, node, start, end):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    tree[node] = init(arr, tree, node*2, start,(start+end)//2) + init(arr, tree, node*2+1, (start+end)//2+1, end)
    return tree[node]
    
def sum(arr, tree, node, start, end, left, right):
    if left > end or right < start:
        return 0

    if left <= start and end <= right:
        return tree[node]

    return sum(arr, tree, node*2, start, (start+end)//2, left, right) + sum(arr, tree, node*2+1, (start+end)//2+1, end, left, right)

def update(arr, tree, node, start, end, idx, diff):
    if idx < start or idx > end:
        return
    tree[node] += diff
    if start != end:
        update(arr, tree, node*2, start, (start+end)//2, idx, diff)
        update(arr, tree, node*2+1, (start+end)//2+1, end, idx, diff)

N, M, K = input_multiple_int()
arr = []
tree = [0 for _ in range(N*4)]

for _ in range(N):
    arr.append(int(input()))

init(arr, tree, 1, 0, N-1)

for _ in range(M+K):
    a,b,c = input_multiple_int()
    if a == 1:
        diff = c - arr[b-1]
        arr[b-1] = c
        update(arr, tree, 1, 0, N-1, b-1, diff)
    else:
        print(sum(arr, tree, 1, 0, N-1, b-1, c-1))
        

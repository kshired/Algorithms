# https://acmicpc.net/problem/11505
# 구간 곱 구하기

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())
MOD = 1000000007

def init(arr, tree, node, start, end):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    tree[node] = (init(arr, tree, node*2, start,(start+end)//2) * init(arr, tree, node*2+1, (start+end)//2+1, end)) % MOD
    return tree[node]
    
def mult(arr, tree, node, start, end, left, right):
    if left > end or right < start:
        return 1

    if left <= start and end <= right:
        return tree[node]

    return (mult(arr, tree, node*2, start, (start+end)//2, left, right) * mult(arr, tree, node*2+1, (start+end)//2+1, end, left, right)) % MOD 

def update(arr, tree, node, start, end, idx, val):
    if idx < start or idx > end:
        return tree[node]
    if start == end:
        tree[node] = val
        return tree[node]
    if start != end:
        tree[node] = (update(arr, tree, node*2, start, (start+end)//2, idx, val) * update(arr, tree, node*2+1, (start+end)//2+1, end, idx, val))%MOD
        return tree[node]

N, M, K = input_multiple_int()
arr = []
tree = [0 for _ in range(N*4)]

for _ in range(N):
    arr.append(int(input()))

init(arr, tree, 1, 0, N-1)

for _ in range(M+K):
    a,b,c = input_multiple_int()
    if a == 1:
        arr[b-1] = c
        update(arr, tree, 1, 0, N-1, b-1, c)
    else:
        print(mult(arr, tree, 1, 0, N-1, b-1, c-1)%MOD)
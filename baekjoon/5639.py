# https://acmicpc.net/problem/5639
# 이진 검색 트리

import sys
sys.setrecursionlimit(10**6)

pre_order = [] # root -> l -> r

for line in sys.stdin.readlines():
    pre_order.append(int(line.rstrip()))

def solve(l,r):
    if l <= r:
        mid = l + 1
        for i in range(l+1,r+1):
            if pre_order[l] < pre_order[i]:
                mid = i
                break
        
        solve(l+1,mid-1)
        solve(mid,r)
        print(pre_order[l])

solve(0,len(pre_order)-1)
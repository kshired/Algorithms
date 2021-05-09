# https://acmicpc.net/problem/2263
# 트리의 순회

import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**8)

n = int(input())
in_order = list(map(int,input().split()))
post_order = list(map(int,input().split()))
pre_order = []
idx = [0 for _ in range(n+1)]
for i in range(n):
    idx[in_order[i]] = i

'''
in order => left root right
post order => left right root
pre order => root left right
'''

def make_pre_order(left_in, right_in, left_post, right_post):
    if left_in > right_in or left_post > right_post:
        return
    root = post_order[right_post] # post_order에서 제일 오른쪽 -> root
    pre_order.append(root) # root -> pre_order에 넣기
    mid = idx[root] # in_order에서 root 위치
    left = mid - left_in # 분할 기준점
    make_pre_order(left_in, mid - 1, left_post, left_post + left - 1) # left_inorder (root 기준으로 분리), left_postorder (leaf의 개수를 기준으로 분리)
    make_pre_order(mid + 1 , right_in, left_post + left, right_post - 1) # right_inorder (root 기준으로 분리), right_postorder (leaf의 개수를 기준으로 분리)

make_pre_order(0, n-1, 0, n-1)
for i in pre_order:
    print(i, end = ' ')
print()
# https://acmicpc.net/problem/1991
# 트리 순회

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def pre_order_traversal(node):
    if node:
        print(node.value,end='')
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)


def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        print(node.value,end='')
        in_order_traversal(node.right)

def post_order_traversal(node):
    if node:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.value,end='')


N = int(input())
tree = [BinaryTreeNode(chr(ord('A')+i)) for i in range(N)]

for _ in range(N):
    nodes = input().split()
    if nodes[1] != '.':
        tree[ord(nodes[0])-ord('A')].left = tree[ord(nodes[1])-ord('A')]
    if nodes[2] != '.':
        tree[ord(nodes[0])-ord('A')].right = tree[ord(nodes[2])-ord('A')]

pre_order_traversal(tree[0])
print()
in_order_traversal(tree[0])
print()
post_order_traversal(tree[0])
print()